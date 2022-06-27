import string
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse, Http404
from django_tables2 import SingleTableView
from .models import Book, Publisher, User
from .tables import BookTable
from wkhtmltopdf.views import PDFTemplateView
import csv

class BookListView(ListView):
    template_name = 'book/book_list.html'
    model = Book


def csv_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    writer = csv.writer(response)
    for book in Book.objects.all():
        strAuthors = " ".join([author.username for author in book.coauthors.all()])
        writer.writerow([book.id, book.name, book.publisher.name, strAuthors, book.published_date])
    return response

class DetailView(SingleTableView):
    table_class = BookTable
    template_name = 'book/detail.html'

    def get_queryset(self):
        return Book.objects.all()

class PdfSampleView(SingleTableView, PDFTemplateView):
    table_class = BookTable
    filename = 'detail.pdf'
    template_name = 'book/detail.html'

    def get_queryset(self):
        return Book.objects.all()

    def get(self, request, *args, **kwargs):
        response_class = self.response_class
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        try:
            if request.GET.get('as', '') == 'html':
                self.response_class = self.html_response_class
        finally:
            self.response_class = response_class

        if self.get_paginate_by(self.object_list) is not None and hasattr(
                self.object_list, "exists"
            ):
                is_empty = not self.object_list.exists()
        else:
                is_empty = not self.object_list
        if is_empty:
            raise Http404(
                    _("Empty list and “%(class_name)s.allow_empty” is False.")
                    % {
                        "class_name": self.__class__.__name__,
                    }
                )
        context = self.get_context_data()
        return self.render_to_response(context)

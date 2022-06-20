import string
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
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

class PdfSampleView(PDFTemplateView):
    filename = 'detail.pdf'
    template_name = 'book/detail.html'

    def get_queryset(self):
        return Book.objects.all()

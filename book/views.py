from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Publisher, User

class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book
    

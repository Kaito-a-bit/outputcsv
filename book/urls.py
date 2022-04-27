from django.urls import path
from . import views

app_name = "book"
urlpatterns = [
  path('',views.BookListView.as_view(), name='book_list'),
  path('export/', views.csv_export, name='export')
]

from django.urls import path
from . import views
from .views import DetailView, PdfSampleView

app_name = "book"
urlpatterns = [
  path('',views.BookListView.as_view(), name='book_list'),
  path('export/', views.csv_export, name='export'),
  path('detail/', DetailView.as_view(), name='detail'),
  path('pdfoutput/', PdfSampleView.as_view(), name='pdf'),
]

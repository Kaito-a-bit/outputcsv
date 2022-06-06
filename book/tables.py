import django_tables2 as tables
from .models import Book

class BookTable(tables.Table):
    class Meta:
        model = Book
        template_name = 'django_tables2/bootstrap4.html' 
        fields = ("id",'name','publisher','coauthors','published_date',)    # 表示する列column

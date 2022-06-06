from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class Publisher(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="id")
    name = models.CharField(max_length=50, verbose_name="name")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='pub_books', verbose_name="publisher")
    coauthors = models.ManyToManyField(User, 'user_books', verbose_name="coauthors")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="published_date")



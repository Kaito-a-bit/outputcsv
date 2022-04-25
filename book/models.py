from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class Publisher(models.Model):
    name = models.CharField(max_length=50)


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='pub_books')
    coauthors = models.ManyToManyField(User, 'user_books')
    published_date = models.DateTimeField(default=timezone.now)



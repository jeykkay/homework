from django.db import models

from Author.models import Author


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)

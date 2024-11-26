"""
Объект книги:
id (int)
title (str)
author (id)
count (int) - остаток книг на складе
"""

from django.db import models

from authors.models import Author


class Book(models.Model):
    title: str = models.CharField(max_length=256)
    author: str = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    count: int = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

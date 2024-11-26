"""
Объект автор:
id (int)
first_name (str)
last_name (str)
"""

from django.db import models


class Author(models.Model):
    first_name: str = models.CharField(max_length=128)
    last_name: str = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

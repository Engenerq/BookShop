from rest_framework import serializers

from authors.models import Author
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = '__all__'

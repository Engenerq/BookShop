from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from authors.models import Author
from authors.serializ import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = LimitOffsetPagination

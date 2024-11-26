from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from books.models import Book
from books.serializ import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=['post'])
    def buy(self, request, pk=None):
        # получить object проверять поле count если ок то отнять 1 сохранить запись
        book = self.get_object()
        if book.count > 0:
            book.count -= 1
            book.save()
            return Response({'message': 'True'})
        return Response({'message': 'Fuck'}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        # Из req вытащить автора из параметров и применять фильтр к queryset
        author = self.request.data.get('author')
        queryset = super().get_queryset()
        if author is not None:
            queryset = queryset.filter(author=author)

        return queryset

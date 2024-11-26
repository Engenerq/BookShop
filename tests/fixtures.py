import pytest

from authors.models import Author
from books.models import Book


@pytest.fixture
def create_author(db):
    return Author.objects.create(
        first_name='First',
        last_name='Last',
    )


@pytest.fixture
def create_books(db, create_author):
    return Book.objects.create(
        title='Test',
        author=create_author,
        count=10,
    )


@pytest.fixture
def create_many_books(db, create_author):
    def wrapper(count):
        models = []
        for index in range(count):
            models.append(Book.objects.create(
                title=f'Test_{index}',
                author=create_author,
                count=10,
            ))
        return models

    return wrapper

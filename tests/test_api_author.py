import pytest
from django.urls import reverse
from rest_framework import status

from authors.models import Author


@pytest.mark.django_db
def test_author_get(client, create_author):
    # response = client.get('/api/authors/')
    response = client.get(reverse('author-list'))
    data = response.json()
    result = data['results']
    assert response.status_code == status.HTTP_200_OK
    assert result[0]['first_name'] == create_author.first_name
    assert result[0]['books'] == []


@pytest.mark.django_db
def test_author_get_with_book(client, create_books, create_author):
    # response = client.get('/api/authors/')
    response = client.get(reverse('author-list'))
    data = response.json()
    result = data['results']
    assert response.status_code == status.HTTP_200_OK
    assert result[0]['first_name'] == create_author.first_name
    assert result[0]['books'] == [create_books.title]


@pytest.mark.django_db
def test_update_author(client, create_author):
    data = {
        "first_name": "Test_update_author_first_name",
        "last_name": "Test_update_author_last_name",
    }
    # response = client.put(f'/api/authors/{create_author.id}/', data=data)
    response = client.put(reverse(f'author-detail', kwargs={"pk": create_author.id}), data=data)

    assert response.status_code == status.HTTP_200_OK
    create_author.refresh_from_db()
    assert create_author.first_name == data['first_name']
    assert create_author.last_name == data['last_name']

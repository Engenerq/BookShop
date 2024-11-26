import pytest
from rest_framework import status

from books.models import Book


@pytest.mark.django_db
def test_get_book(client, create_books):
    response = client.get("/api/books/")
    data = response.json()
    result = data['results']
    assert response.status_code == status.HTTP_200_OK
    assert result[0]['title'] == create_books.title, data


@pytest.mark.django_db
def test_get_book(client, create_many_books):
    books_create = create_many_books(10)
    response = client.get("/api/books/", data={"limit": 5, "offset": 0})
    data = response.json()
    result = data['results']
    assert response.status_code == status.HTTP_200_OK
    assert len(result) == 5
    response_2 = client.get("/api/books/", data={"limit": 5, "offset": 5})
    data = response_2.json()
    result_2 = data['results']
    assert response_2.status_code == status.HTTP_200_OK
    assert len(result_2) == 5
    books = [book['title'] for book in (*result, *result_2)]
    for book in books_create:
        assert book.title in books, books


@pytest.mark.django_db
def test_filter_get_book(client, create_books, create_author):
    response = client.get(f"/api/books/?author={create_author.id}")
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    result = data['results']
    assert len(result) == 1
    assert result[0]['title'] == create_books.title


@pytest.mark.django_db
def test_create_book(client, create_author):
    data = {
        "title": "Test_create_book",
        "author": create_author.id,
        "count": 20,
    }

    response = client.post("/api/books/", data=data)

    assert response.status_code == status.HTTP_201_CREATED
    assert Book.objects.filter(title=data["title"]).exists()


@pytest.mark.django_db
def test_update_book(client, create_books):
    data = {
        "title": "Test_update_book",
        "author": create_books.author.id,
        "count": 10,
    }
    response = client.put(f"/api/books/{create_books.id}/", data=data)

    assert response.status_code == status.HTTP_200_OK

    create_books.refresh_from_db()

    assert create_books.title == data["title"]
    assert create_books.author.id == data["author"]
    assert create_books.count == data["count"]


@pytest.mark.django_db
def test_buy_book(client, create_books):
    data_count = create_books.count
    response = client.post(f"/api/books/{create_books.id}/buy/")

    assert response.status_code == status.HTTP_200_OK

    create_books.refresh_from_db()

    assert data_count == create_books.count + 1


@pytest.mark.django_db
def test_zero_book(client, create_books):
    create_books.count = 0
    create_books.save()
    response = client.post(f"/api/books/{create_books.id}/buy/")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()['message'] == 'Fuck'

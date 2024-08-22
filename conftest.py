import pytest
from main import BooksCollector


@pytest.fixture
def book():
    return BooksCollector()

@pytest.fixture
def populated_book(book):
    book.add_new_book('Лавр')
    book.set_book_genre('Лавр', 'Фантастика')
    book.add_new_book('Зов кукушки')
    book.set_book_genre('Зов кукушки', 'Детективы')
    book.add_new_book('Оно')
    book.set_book_genre('Оно', 'Ужасы')
    book.add_new_book('Летучий корабль')
    book.set_book_genre('Летучий корабль', 'Мультфильмы')
    book.add_new_book('Чемодан')
    book.set_book_genre('Чемодан', 'Комедии')
    return book

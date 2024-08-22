import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_initial_books_genre_is_empty_dict(self, book):
        assert book.books_genre == {}

    def test_initial_favorites_is_empty_list(self, book):
        assert book.favorites == []

    def test_add_new_book_short_name_added(self, book):
        book.add_new_book('Лавр')
        assert book.books_genre['Лавр'] == ''

    def test_set_book_genre_added_book_genre_is_set(self, book):
        book.add_new_book('Лавр')
        book.set_book_genre('Лавр', 'Фантастика')
        assert book.books_genre['Лавр'] == 'Фантастика'

    def test_get_book_genre_added_book_return_book_genre(self, populated_book):
        assert populated_book.get_book_genre('Лавр') == 'Фантастика'

    @pytest.mark.parametrize(
        'name,genre',
        [
            ['Лавр', 'Фантастика'],
            ['Оно', 'Ужасы'],
            ['Зов кукушки', 'Детективы'],
            ['Летучий корабль', 'Мультфильмы'],
            ['Чемодан', 'Комедии']
        ]
    )
    def test_get_books_with_specific_genre_add_new_book_with_genre_return_this_book(self, populated_book, name, genre):
        assert name in populated_book.get_books_with_specific_genre(genre)

    def test_get_books_genre_added_book_without_genre_return_name_only(self, book):
        book.add_new_book('Лавр')
        assert book.get_books_genre() == {'Лавр': ''}

    @pytest.mark.parametrize('name', ['Оно', 'Зов кукушки'])
    def test_get_books_for_children_populated_book_return_list_exept_genre_age_rating(self, populated_book, name):
        assert name not in populated_book.get_books_for_children()

    def test_add_book_in_favorites_existed_book_apeears_in_favorites_list(self, populated_book):
        populated_book.add_book_in_favorites('Чемодан')
        assert 'Чемодан' in populated_book.favorites

    def test_delete_book_from_favorites_remove_book_this_book_unlisted(self, populated_book):
        populated_book.add_book_in_favorites('Чемодан')
        populated_book.delete_book_from_favorites('Чемодан')
        assert 'Чемодан' not in populated_book.favorites

    def test_get_list_of_favorites_books_add_two_books_list_of_two_books(self, populated_book):
        populated_book.add_book_in_favorites('Зов кукушки')
        populated_book.add_book_in_favorites('Лавр')
        assert populated_book.get_list_of_favorites_books() == ['Зов кукушки', 'Лавр']

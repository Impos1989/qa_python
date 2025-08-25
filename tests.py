from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()
    
    # Тесты init
    def test_init_books_genre_is_empty_dict(self, collector):
        assert collector.books_genre == {}

    def test_init_favorites_is_empty_list(self, collector):
        assert collector.favorites == []

    def test_init_genre_contains_expected_values(self, collector):
        expected_genre = ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"]
        assert collector.genre == expected_genre

    def test_init_genre_age_rating_contains_expected_values(self, collector):
        expected_age_rating = ["Ужасы", "Детективы"]
        assert collector.genre_age_rating == expected_age_rating

    # Тесты add_new_book
    @pytest.mark.parametrize("book_name", ["", "a" * 41])
    def test_add_new_book_invalid_length_name_does_not_add(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_adds_multiple_books(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_does_not_add_duplicate(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 1")
        assert len(collector.get_books_genre()) == 1

    # Тесты set_book_genre
    def test_set_book_genre_sets_valid_genre(self, collector):
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Фантастика")
        assert collector.get_book_genre("Книга") == "Фантастика"

    def test_set_book_genre_does_not_affect_nonexistent_book(self, collector):
        collector.set_book_genre('Несуществующая книга', 'Ужасы')
        assert 'Несуществующая книга' not in collector.get_books_genre()

    def test_set_book_genre_does_not_set_invalid_genre(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Несуществующий жанр')
        assert collector.get_book_genre('Книга') == ''

    # Тесты get_book_genre
    def test_get_book_genre_returns_correct_genre(self, collector):
        collector.add_new_book("Смешная книга")
        collector.set_book_genre("Смешная книга", "Комедии")
        assert collector.get_book_genre("Смешная книга") == "Комедии"
        
    def test_get_book_genre_without_genre(self, collector):
        collector.add_new_book("Книга без жанра")
        assert collector.get_book_genre("Книга без жанра") == ""

    def test_get_book_genre_nonexistent_book_return_none(self, collector):
        assert collector.get_book_genre("Несуществующая книга") is None

    # Тесты get_books_with_specific_genre
    def test_get_books_with_specific_genre_return_books_by_genre(self, collector):
        collector.add_new_book("Книга 1")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 2", "Фантастика")
        collector.add_new_book("Книга 3")
        collector.set_book_genre("Книга 3", "Ужасы")
        books = collector.get_books_with_specific_genre("Фантастика")
        assert books == ["Книга 1", "Книга 2"]

    def test_get_books_with_specific_genre_no_matches_return_empty_list(self, collector):
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Комедии")
        books = collector.get_books_with_specific_genre("Фантастика")
        assert books == []

    # Тесты get_books_genre
    def test_get_books_genre_return_dict(self, collector):
        collector.add_new_book("Книга")
        collector.set_book_genre("Книга", "Фантастика")
        assert collector.get_books_genre() == {"Книга": "Фантастика"}

    # Тесты get_books_for_children
    @pytest.mark.parametrize(
        "books_data, expected_children_books",
        [
            (
                [("Книга 1", "Фантастика"), ("Книга 2", "Мультфильмы")],
                ["Книга 1", "Книга 2"],
            ),
            ([("Книга 1", "Комедии"), ("Книга 2", "Ужасы")], ["Книга 1"]),
            ([("Книга 1", "Ужасы"), ("Книга 2", "Детективы")], []),
            ([("Книга 1", "")], []),
            ([], []),
        ],
    )
    def test_get_books_for_children_returns_only_books_for_children(
        self, collector, books_data, expected_children_books
    ):
        for name, genre in books_data:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        books = collector.get_books_for_children()
        assert sorted(books) == sorted(expected_children_books)

    # Тесты add_book_in_favorites
    def test_add_book_in_favorites_adds_book_to_favorites(self, collector):
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        assert "Книга" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_does_not_add_nonexistent_book(self, collector):
        collector.add_book_in_favorites("Несуществующая книга")
        assert "Несуществующая книга" not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_does_not_add_duplicate(self, collector):
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.add_book_in_favorites("Книга")
        assert len(collector.get_list_of_favorites_books()) == 1

    # Тесты delete_book_from_favorites
    def test_delete_book_from_favorites_removes_book_from_favorites(self, collector):
        collector.add_new_book("Книга")
        collector.add_book_in_favorites("Книга")
        collector.delete_book_from_favorites("Книга")
        assert "Книга" not in collector.get_list_of_favorites_books()

    # Тесты get_list_of_favorites_books
    def test_get_list_of_favorites_books_return_favorites_list(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.add_new_book("Книга 3")
        collector.add_book_in_favorites("Книга 1")
        collector.add_book_in_favorites("Книга 2")
        assert collector.get_list_of_favorites_books() == ["Книга 1", "Книга 2"]

    def test_get_list_of_favorites_books_return_empty_list_when_no_favorites(
        self, collector
    ):
        assert collector.get_list_of_favorites_books() == []

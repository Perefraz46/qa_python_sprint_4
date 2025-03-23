from main import BooksCollector


class TestBooksCollector:

    @pytest.mark.parametrize(
        'name, expected',
        [
            ('Горе от ума', True),  # Корректное название
            ('', False),            # Пустое название
            ('A' * 41, False),      # Название длиннее 40 символов
        ]
    )
    def test_add_new_book_with_valid_name_should_add_book(self, name, expected):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert (name in collector.books_genre) == expected

    def test_set_book_genre_with_valid_book_and_genre_should_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('Горе от ума', 'Комедии')
        assert collector.get_book_genre('Горе от ума') == 'Комедии'

    def test_get_book_genre_for_existing_book_should_return_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('Горе от ума', 'Комедии')
        assert collector.get_book_genre('Горе от ума') == 'Комедии'

    def test_get_books_with_specific_genre_should_return_correct_books(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.add_new_book('Мёртвые души')
        collector.set_book_genre('Горе от ума', 'Комедии')
        collector.set_book_genre('Мёртвые души', 'Комедии')
        assert collector.get_books_with_specific_genre('Комедии') == ['Горе от ума', 'Мёртвые души']

    def test_get_books_genre_should_return_all_books_with_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('Горе от ума', 'Комедии')
        assert collector.get_books_genre() == {'Горе от ума': 'Комедии'}

    def test_get_books_for_children_should_return_books_without_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.add_new_book('Мёртвые души')
        collector.set_book_genre('Горе от ума', 'Комедии')
        collector.set_book_genre('Мёртвые души', 'Ужасы')
        assert collector.get_books_for_children() == ['Горе от ума']

    def test_add_book_in_favorites_with_existing_book_should_add_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.add_book_in_favorites('Горе от ума')
        assert 'Горе от ума' in collector.favorites

    def test_delete_book_from_favorites_should_remove_book(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.add_book_in_favorites('Горе от ума')
        collector.delete_book_from_favorites('Горе от ума')
        assert 'Горе от ума' not in collector.favorites

    def test_get_list_of_favorites_books_should_return_all_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Горе от ума')
        collector.add_new_book('Мёртвые души')
        collector.add_book_in_favorites('Горе от ума')
        collector.add_book_in_favorites('Мёртвые души')
        assert collector.get_list_of_favorites_books() == ['Горе от ума', 'Мёртвые души']
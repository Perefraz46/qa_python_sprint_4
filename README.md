# qa_python
1) test_add_new_book_with_valid_name_should_add_book - Проверяем, что книга добавляется в словарь books_genre, если её название соответствует ограничениям.
2) test_set_book_genre_with_valid_book_and_genre_should_set_genre - Проверяем, что жанр книги устанавливается корректно, если книга и жанр существуют.
3) test_get_book_genre_for_existing_book_should_return_genre - Проверяем, что метод возвращает правильный жанр книги.
4) test_get_books_with_specific_genre_should_return_correct_books - Проверяем, что метод возвращает список книг с определённым жанром.
5) test_get_books_genre_should_return_all_books_with_genres - Проверяем, что метод возвращает весь словарь books_genre.
6) test_get_books_for_children_should_return_books_without_age_rating - Проверяем, что метод возвращает книги без возрастного рейтинга.
7) test_add_book_in_favorites_with_existing_book_should_add_to_favorites - Проверяем, что книга добавляется в избранное, если она есть в books_genre.
8) test_delete_book_from_favorites_should_remove_book - Проверяем, что книга удаляется из избранного.
9) test_get_list_of_favorites_books_should_return_all_favorites - Проверяем, что метод возвращает список избранных книг.

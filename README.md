1. test_init_books_genre_is_empty_dict - проверка, что books_genre - пустой словарь
2. test_init_favorites_is_empty_list - проверка, что favorites - пустой список
3. test_init_genre_contains_expected_values - проверка, что genre содержит ожидаемые значения
4. test_init_genre_age_rating_contains_expected_values - проверка, что genre_age_rating содержит ожидаемые значения
5. test_add_new_book_invalid_length_name_does_not_add - проверка, что книги с недопустимой длиной названия не добавляются
6. test_add_new_book_adds_multiple_books - проверка добавления нескольких книг
7. test_add_new_book_does_not_add_duplicate - проверка, что дубликаты книг не добавляются
8. test_set_book_genre_sets_valid_genre - проверка установки допустимого жанра
9. test_set_book_genre_does_not_affect_nonexistent_book - проверка, что установка жанра не влияет на несуществующую книгу
10. test_set_book_genre_does_not_set_invalid_genre - проверка, что недопустимый жанр не устанавливается
11. test_get_book_genre_returns_correct_genre -  проверка возврата правильного жанра книги
12. test_get_book_genre_without_genre - проверка возврата пустого значения жанра, если жанр не устанавливался
13. test_get_book_genre_nonexistent_book_return_none - проверка возврата None для несуществующей книги
14. test_get_books_with_specific_genre_return_books_by_genre - проверка возврата книг с определенным жанром
15. test_get_books_with_specific_genre_no_matches_return_empty_list - проверка возврата пустого листа, если нет совпадений по жанру
16. test_get_books_genre_return_dict - проверка возврата правильного словаря книг
17. test_get_books_for_children_returns_only_books_for_children - параметризованная проверка возврата только детских книг
18. test_add_book_in_favorites_adds_book_to_favorites - проверка добавления книги в избранное
19. test_add_book_in_favorites_does_not_add_nonexistent_book - проверка, что несуществующая книга не добавляется в избранное
20. test_add_book_in_favorites_does_not_add_duplicate - проверка, что дубликаты не добавляются в избранное
21. test_delete_book_from_favorites_removes_book_from_favorites - проверка удаления книги из избранного
22. test_get_list_of_favorites_books_return_favorites_list - проверка возврата списка избранных книг
23. test_get_list_of_favorites_books_return_empty_list_when_no_favorites - проверка возврата пустого списка, когда нет избранных книг

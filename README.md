# Тест-кейсы для BooksCollector

## Описание проекта
`BooksCollector` — это класс, который позволяет установить жанр книг и добавить их в избранное. 

## Тест-кейсы

### 1. Проверка инициализации `books_genre`
- **Описание:** Убедиться, что `books_genre` инициализируется как пустой словарь.
- **Тест:** `test_initial_books_genre_is_empty_dict`

### 2. Проверка инициализации `favorites`
- **Описание:** Убедиться, что `favorites` инициализируется как пустой список.
- **Тест:** `test_initial_favorites_is_empty_list`

### 3. Проверка добавления новой книги
- **Описание:** Убедиться, что новая книга добавилась в библиотеку `books_genre` с пустым значением
- **Тест:** `test_add_new_book_short_name_added`

### 4. Проверка установки жанра книге
- **Описание:** Убедиться, что мы можем в `books_genre` добавить жанр уже существующей книге
- **Тест:** `test_set_book_genre_added_book_genre_is_set`

### 5. Проверка выдачи жанра по названию книги
- **Описание:** Убедиться, что можем получить жанр по имени из `books_genre`
- **Тест:** `test_get_book_genre_added_book_return_book_genre`

### 6. Проверка выдачи книг по жанру
- **Описание:** Убедиться, что можем получить книги по жанру
- **Тест:** `test_get_books_with_specific_genre_add_new_book_with_genre_return_this_book`

### 7. Проверка получения словаря `books_genre`
- **Описание:** Убедиться, что работает метод получения словаря `books_genre` с именем книги без жанра
- **Тест:** `test_get_books_genre_added_book_without_genre_return_name_only`

### 8. Проверка фильтра книг для детей
- **Описание:** Убедиться, в списке книг для детей нет ужасов и детективов
- **Тест:** `test_get_books_for_children_populated_book_return_list_exept_genre_age_rating`

### 9. Проверка добавления книги в Избранное
- **Описание:** Убедиться что книга добавляется в Избранное
- **Тест:** `test_add_book_in_favorites_existed_book_apeears_in_favorites_list`

### 10. Проверка удаления книги из Избранного
- **Описание:** Убедиться что книга удаляется из Избранного
- **Тест:** `test_delete_book_from_favorites_remove_book_this_book_unlisted`

### 11. Проверка получения списка книг из Избранного
- **Описание:** Убедиться что мы можем получить список книг из Избранного
- **Тест:** `test_get_list_of_favorites_books_add_two_books_list_of_two_books`
- 
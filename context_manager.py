import json
import csv


# Чтение и сохранение данных файла с книгами в список
with open('books.csv') as books:
    book_list = []
    csv_reader = csv.DictReader(books)
    for row in csv_reader:
        book_list.append(row)

# Чтение и сохранение полученного списка в словарь json
with open('books_dictionary.json', 'w') as books_json:
    json.dump(book_list, books_json, sort_keys=True, indent=4)

# Чтение и запись файла с книгами и пользователями в формате json
with open('books_dictionary.json') as books_dictionary_json:
    books_data = json.load(books_dictionary_json)
    for book in books_data:
        with open('users.json', 'r') as user_json:
            users_data = json.load(user_json)
            results_data = []
            for item in users_data:
                results_data.append(
                    {'name': item["name"], 'gender': item["gender"], 'address': item["address"], 'books': book})

    with open('users_and_books.json', 'w') as users_and_books:
        json.dump(results_data, users_and_books, sort_keys=True, indent=4)

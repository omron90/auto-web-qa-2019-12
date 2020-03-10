from contextlib import contextmanager
import json
import csv


@contextmanager
def file_open(path, flag):
    global f_object
    try:
        f_object = open(path, flag)
        yield f_object  # Возвращение объекта
    except OSError:
        print("Файл не доступен!")
    finally:
        f_object.close()


if __name__ == '__main__':
    books = []
    users = []

    """ Чтение books.csv и заполнение books[] """
    with file_open('source/books.csv', 'r') as csv_file:
        reader_books = csv.DictReader(csv_file, delimiter=',')
        for line in reader_books:
            title = line['Title']
            author = line['Author']
            height = line['Height']
            books.append({'title': title, 'author': author, 'height': height})

    """ Чтение users.json и заполнение users[] """
    with file_open('source/users.json', 'r') as json_file:
        reader_users = json.load(json_file)
        for user in reader_users:
            users.append({'name': user["name"], 'gender': user["gender"], 'address': user["address"], 'books': {}})

    """ Редактирование JSON(users[]) и запись в result.json """
    new_data = json.loads(json.dumps(users))
    i = 0
    for init in new_data:
        init['books'] = [books[i]]
        i += 1

    with file_open('source/complete.json', 'w') as result:
        result.write(json.dumps(new_data, indent=2))

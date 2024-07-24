import json
from class_library_book import Book, Library


def _get_new_book_data() -> tuple:
    """Функция ввода данных от пользователя, для создания или поиска книг
    проверяет вводимые данные и возвращает кортеж"""

    try:
        title = input("Введите название книги: \n")
        if not title:
            title = None
        author = input("Введите автора книги: \n")
        if not author:
            author = None
        year = input("Введите год издания книги: \n")
        if not year:
            year = None
        year = int(year)
    except TypeError:
        pass
    return (title, author, year)


def _create_book(value: Library):
    print("Для добавления книги, введите ее данные\n"
          "обращаю ваше внимание, что все данные о книге должны быть заполнены название/автор/год(в формате числа)\n")
    if input_result := _get_new_book_data():
        title, author, year = input_result
        if existed_book := value._find_book(title, author, year):
            raise ValueError(f"Такая книга существует id ={existed_book[0].id}\n")
        book = Book(title, author, year)
        value.dict_books[book.id] = book
        value._write_json()
    else:
        _create_book(value)


def _delete_book(value: Library):
    id_book = int(input("Введите номер книги в библиотеке\n"))
    print("---------------------")
    print(f"Книга {value._delete_book(id_book).title} удалена\n")
    print("---------------------")
    value._write_json()


def _find_library_book(value: Library):
    """Функция принмает от пользователя данные об искомой книге и вызывает метод класса Library._find_book
    Если полученные от метода список содержит элементы, выводит их
    иначе сообщает что книги не найдены"""

    print("Введите название, автора или год издания книги"
          "если что - то не известно - пропустите, нажав Ввод\n")
    title, author, year = _get_new_book_data()
    book_list = value._find_book(title, author, year)
    if book_list:
        print("По заданным параметрам нашлись книги:\n")
        for book in book_list:
            print("---------------------")
            print(book.__str__())
            print("---------------------")
    else:
        print("Книжек с такими параметрами не нашлось")


def _chenge_status_library_book(value: Library):
    """Функция принмает от пользователя данные и выдывает метод класса Book._change_status
    изменения записывает в JSON-файл"""

    id_book = int(input("Введите номер книги в библиотеке, у которой хотите изменить статус\n"))
    new_status = input("Введите новый статус книги\n")
    value._get_by_id(id_book)._change_status(new_status)
    value._write_json()
    print(f"Статус книги {value.dict_books[id_book].title} изменен \n")


def _read_json(json_name: str = "Library") -> list[dict]:
    """Парсит JSON-файл и возвращает список словарей
    Если файла нет в папке с проектом, вызовет исключение FileNotFoundError"""

    with open(json_name, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def _create_library(value: Library):
    """Функция подгрузки данных из JSON- файла, если таковой существует.
     Проходит циклом по _read_json и создает экземпляры класса Book, с учетом идентификаторов и статуса книги
     повышает счетчик идентификатора класса книги через _generate_id, чтобы новая книга, была со следующим порядковым номером"""

    for book in _read_json():
        title, author, year = book.get("title"), book.get("author"), book.get("year")
        old_book = Book(title, author, year)
        old_book._change_status(book.get("status"))
        old_book._set_id(int(book.get("id")))
        value.dict_books[old_book.id] = old_book
    old_book._generate_id(last_id= old_book.id)


    print("В библиотеке есть несколько книжек")

import json

_default_json_name = "Library"


class Book:
    """ Класс Book используется для создания книги по переданным аргументам
    Attributes
    -----------
    _valid_status - список значений поля status, использкентся для проверки ввода
    _id - порядковый номер экземпляра книги, увеличивается на один, после добавления нового экземпляра
    """

    _valid_status = ["в наличии", "выдана", ]
    _id = 0

    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"
        self.id = self._generate_id()

    def __str__(self):
        return (f"инедтификатор - {self.id}\n"
                f"Название книги - {self.title}\n"
                f"Автор книги - {self.author}\n"
                f"Год публикации - {self.year}\n"
                f"Наличие в библиотеке - {self.status}\n")

    def _change_status(self, status: str) -> None:
        if status in self._valid_status:
            self.status = status
        else:
            raise ValueError(f"Статус {status} запрещен\n")

    def _set_id(self, id: int) -> int:
        self.id = id

    def _generate_id(self) -> int:
        Book._id += 1
        return Book._id

    def _get_dict_book(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }


class Library:
    """
    Класс Library служит хранилищем (библиотекой) для экземпляров класса Book (книг)
    Attributes
    -----------
    self.dict_books - словарь, в котором ключем является идентификатор экземпляра класса Book, а значением ключа
    соответственно сам экземпляр класса Book

    Methods
    -------
    _find_book() - принимает на вход строковые значения для автора и названия книга, целочисленные значение для года
    По полученным параметрам ищет книги в библиотеке, и возвращает списог книг, если они есть
    если нет - пустой список

    _get_by_id() - метод проверяет, есть ли книга в библиотеке с введенным индексом

    _show_all_book() - итерируется по всем книжкам библиотеки и вызывает у них метод ___str___()

    _delete_book() - возвращает и удаляет из словаря self.dict_books значение по переданному ключу,
    выбрасывает исключение KeyError если ключа не будет

    _write_json() - записывает/перезаписывает JSON-файл, вызывается при каком - либо изменении словаря self.dict_books
    """

    def __init__(self) -> dict:
        self.dict_books = {}

    def _find_book(self, title: str | None = None, author: str | None = None, year: int | None = None) -> list:
        _search_result = []
        for val in self.dict_books.values():
            if (title is None or val.title == title) and \
                    (author is None or val.author == author) and \
                    (year is None or val.year == year):
                _search_result.append(val)
        return _search_result

    def _get_by_id(self, id: int) -> dict:
        if not self.dict_books.get(id):
            raise KeyError(f"Книги с номером {id} не существует ")
        else:
            result = self.dict_books.get(id)
        return result

    def _show_all_book(self):
        if self.dict_books.values():
            print(f"Ниже представлены все книги в нашей библиотеке:\n")
            print("---------------------")
            for book in self.dict_books.values():
                print(book.__str__())
                print("---------------------\n")
        else:
            print("В библиотеке пока нет книг\n")

    def _delete_book(self, id: int) -> dict:
        if self._get_by_id(id):
            return self.dict_books.pop(id)

    def _write_json(self, json_name: str = _default_json_name):
        json_list = []
        for val in self.dict_books.values():
            json_list.append(val._get_dict_book())
        with open(json_name, "w", encoding="utf-8") as write_file:
            json.dump(json_list, write_file, ensure_ascii=False, indent=4)


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
    id_book = int(input("Введите номер книжки в библиотеке\n"))
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

    id_book = int(input("Введите номер книжки в библиотеке, у которой хотите изменить статус"))
    new_status = input("Введите новый статус книги\n")
    value._get_by_id(id_book)._change_status(new_status)
    value._write_json()
    print(f"Статус книги {value.dict_books[id_book].title} изменен \n")


def _read_json(json_name: str = _default_json_name) -> list[dict]:
    """Парсит JSON-файл и возвращает список словарей
    Если файла нет в папке с проектом, вызовет исключение FileNotFoundError"""

    with open(json_name, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def _create_library(value: Library):
    """Функция подгрузки данных из JSON- файла, если таковой существует.
     Проходит циклом по _read_json и создает экземпляры класса Book, с учетом идентификаторов и статуса книги"""

    for book in _read_json():
        title, author, year = book.get("title"), book.get("author"), book.get("year")
        old_book = Book(title, author, year)
        old_book._change_status(book.get("status"))
        old_book._set_id(int(book.get("id")))
        value.dict_books[old_book.id] = old_book
    print("В библиотеке есть несколько книжек")


def main(value):
    try:
        _create_library(value)
    except FileNotFoundError:
        print("Давайте создадим новую библиотеку!")
    """
    Функция, которая связывает между собой два класса Library и Book, организовывает добавление, удаление книг из библиотеки
    изменение статуса книги, вывод всех книг библиотеки и поиск по ним. Принимает от пользователя аргументы, в соответствии с которыми запускает работу определенных методов
    """

    while True:
        print("Выберите действия:\n"
              "Добавить книгу - введите 1\n"
              "Удалить книгу - введите 2\n"
              "Найти книгу - введите 3\n"
              "Показать все книги в библиотеке - введите 4\n"
              "Изменить статус книги - введите 5\n"
              "Для выхода введите 0\n")
        command = input("Введите номер команды: ")

        try:
            match command:
                case '1':
                    _create_book(value)
                case '2':
                    _delete_book(value)
                case '3':
                    _find_library_book(value)
                case '4':
                    value._show_all_book()
                case '5':
                    _chenge_status_library_book(value)
                case '0':
                    exit()
                case _:
                    print("Незнакомая команда, повторите ввод")
        except ValueError as e:
            print("Не верный ввод данных")
            print(e)
        except KeyError as e:
            print(e)


if __name__ == '__main__':
    lib = Library()
    main(lib)

import json


class Book:
    """ Класс Book используется для создания книги по переданным аргументам
    Attributes
    -----------
    _valid_status - список допустимых значений поля status, использкентся для проверки ввода
    _id - порядковый номер экземпляра книги, увеличивается на один, после добавления нового экземпляра

    Methods
    -------
     __str__() - возвращает строковое представление аргументов класса Book

    _change_status() - метод меняет статус книги, в наличии/выдана сравнивая полученное значение со списком допустимых значений _valid_status

    _set_id() - метод устанавливает значение id экземпляра класса, если в JSON - файл уже существует и нужно добавить книги из него

    _generate_id() - метод увеличения счетчка id  с добавлением каждой новой книги

    _get_dict_book() - возвращает словарь, где ключами являются имена атрибутов, а значениями соответственно значение этих атрибутов в экземпляре класса

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

    def _generate_id(self, last_id = None) -> int:
        if last_id:
            Book._id = last_id
        else:
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

    def _write_json(self, json_name: str = "Library"):
        json_list = []
        for val in self.dict_books.values():
            json_list.append(val._get_dict_book())
        with open(json_name, "w", encoding="utf-8") as write_file:
            json.dump(json_list, write_file, ensure_ascii=False, indent=4)

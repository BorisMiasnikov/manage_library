class Book:
    _valid_status = ["в наличии", "выдана", ]
    _id = 0

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"
        self.id = self.generate_id()

    def __str__(self):
        return (f"инедтификатор - {self.id}\n"
                f"Название книги - {self.title}\n"
                f"Автор книги - {self.author}\n"
                f"Год публикации - {self.year}\n"
                f"Наличие в библиотеке - {self.status}\n")

    def change_status(self, status: str) -> None:
        if status in self._valid_status:
            self.status = status
        else:
            raise ValueError(f"Статус {status} запрещен")

    def generate_id(self):
        Book._id += 1
        return Book._id


class Library:
    def __init__(self):
        self.dict_books = {}

    def find_book(self, title: str | None = None, author: str | None = None, year: int | None = None) -> list:
        search_result = []
        for val in self.dict_books.values():
            if (title is None or val.title == title) and \
                    (author is None or val.author == author) and \
                    (year is None or val.year == year):
                search_result.append(val)
        return search_result

    def show_all_book(self):
        if self.dict_books.values():
            print(f"Ниже представлены все книги в нашей библиотеке:\n")
            for book in self.dict_books.values():
                print(book.__str__())
                print("|||||||||/////___")
        else:
            print("В библиотеке пока нет книг")

    def delete_book(self, id: int):
        return self.dict_books.pop(id)


def main(value):
    while True:
        print("Выберите действия:\n"
              "Добавить книгу - введите 1\n"
              "Удалить книгу - введите 2\n"
              "Найти книгу - введите 3\n"
              "Показать все книги в библиотеке - введите 4\n"
              "Изменить статус книги - введите 5\n"
              "Для выхода введите 0\n")
        command = input("Введите номер команды: ")
        match command:
            case '1':
                while True:
                    print("Для добавления книги, введите ее данные\n"
                          "обращаю ваше внимание, что все данные о книге должны быть заполнены название/автор/год(в формате числа)")
                    try:
                        title = input("Введите название книги: ")
                        if not title:
                            raise ValueError("Название не может быть пустым")
                        author = input("Введите Автора книги: ")
                        if not author:
                            raise ValueError("У книги должен быть автор ")
                        year = int(input("Введите год издания книги: "))
                        if year < 1:
                            raise ValueError("Все, что издавалось до рождества христова, в нашу библиотеку не вхоже")
                    except ValueError:
                        print("Вы ввели не коректные данные, повторите ввод сначала")
                        continue
                    else:
                        break
                for val in value.dict_books.values():
                    if val.title == title and val.author == author and val.year == year:
                        print(f"Такая книга уже есть в библиотеке под номером {val.id}")
                        break
                else:
                    book = Book(title, author, year)
                    value.dict_books[book.id] = book
            case '2':
                try:
                    id_book = int(input("Введите номер книжки в библиотеке"))
                    if id_book < 1:
                        raise ValueError
                    print(f"Книга {value.delete_book(id_book).title} удалена")
                except ValueError:
                    print("Вы ввели не коректные данные")
                except KeyError:
                    print("Такой книги нет в библиотеке")
            case '3':
                print("Введитте название, автора или год издания книги\n"
                      "если что - то не известно - пропустите, нажав Ввод")
                try:
                    title = input("Введите название книги: ")
                    if not title:
                        title = None
                    author = input("Введите Автора книги: ")
                    if not author:
                        author = None
                    year = input("Введите год издания книги: ")
                    if not year:
                        year = None
                    year = int(year)
                    if year < 1:
                        raise ValueError("Все, что издавалось до рождества христова, в нашу библиотеку не вхоже")
                except TypeError:
                    pass
                except ValueError:
                    print("Вы ввели не коректные данные, повторите ввод сначала")
                for book in value.find_book(title, author, year):
                    print(book.__str__())
                    print("|||||||||/////___")
            case '4':
                value.show_all_book()
            case '5':
                try:
                    id_book = int(input("Введите номер книжки в библиотеке, у которой хотите изменить статус"))
                    new_status = input("Введите новый статус книги")
                    if id_book < 1:
                        raise ValueError
                except ValueError:
                    print("Вы ввели не коректные данные")
                except KeyError:
                    print("Такой книги нет в библиотеке")
                try:
                    value.dict_books[id_book].change_status(new_status)
                    print(f"Статус книги {value.dict_books[id_book].title} изменен ")
                except ValueError:
                    print("Такого статуса нет")
            case '0':
                exit()
            case _:
                print("Незнакомая команда, повторите ввод")


x = Library()
title = "Книга "
author = "Автор"
year = 1
for i in range(10):
    title += str(i)
    author += str(i)
    year += i
    book = Book(title, author, year)
    x.dict_books[book.id] = book
main(x)

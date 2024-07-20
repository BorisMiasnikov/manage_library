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
            if (title is None or book.title == title) and \
                    (author is None or book.author == author) and \
                    (year is None or book.year == year):
                search_result.append(book)
        return looking_book

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
                            raise ValueError("Все, что издавалось до рождества христова, в нишу библиотеку не вхоже")
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
                pass
            case '4':
                value.show_all_book()
            case '5':
                pass
            case '0':
                exit()
            case _:
                print("Незнакомая команда, повторите ввод")


x = Library()
main(x)

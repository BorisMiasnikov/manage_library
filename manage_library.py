_id = 1  # счетчик будет увеличиваться в функции вызова создания объекта модели
_list_books = {}
_valid_status = ["в наличии", "выдана", ]


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.id = _id
        self.status = "в наличии"

    def change_status(self, status: str) -> None:
        if status in _valid_status:
            self.status = status
        else:
            raise ValueError(f"Статус {status} запрещен")


def find_book(title: str | None = None, author: str | None = None, year: int | None = None) -> list:
    looking_book = []
    if not title:
        for val in _list_books.values():
            if val.title == title:
                looking_book.append(val)
    elif not author:
        if not looking_book:
            for val in _list_books.values():
                if val.author == author:
                    looking_book.append(val)
        else:
            for book in looking_book:
                if book.author == author:
                    looking_book.append(book)
    elif not year:
        if not looking_book:
            for val in _list_books.values():
                if val.year == year:
                    looking_book.append(val)
        else:
            for book in looking_book:
                if book.year == year:
                    looking_book.append(book)
    return looking_book


def show_all_book():
    if _list_books.values():
        print(f"Ниже представлены все книги в нашей библиотеке:\n")
        for book in _list_books.values():
                print(f"инедтификатор - {book.id}\n"
                    f"Название книги - {book.title}\n"
                    f"Автор книги - {book.author}\n"
                    f"Год публикации - {book.year}\n"
                    f"Наличие в библиотеке - {book.status}\n"
                    f"_____________________________\n")
    else:
        print("В библиотеке пока нет книг")


def delete_book(id: int):
    return _list_books.pop(id)


def main():
    choice_value = [1, 2, 3, 4, 5, 0]
    global _id
    while True:
        print("Выберите действия:\n"
              "Добавить книгу - введите 1\n"
              "Удалить книгу - введите 2\n"
              "Найти книгу - введите 3\n"
              "Показать все книги в библиотеке - введите 4\n"
              "Изменить статус книги - введите 5\n"
              "Для выхода введите 0\n")
        try:
            user_choice = int(input("Пожалуйста введите номер действия - "))
            if user_choice not in choice_value:
                raise ValueError("Нет такого значения")
        except ValueError:
            print("Не верный ввод, вводите пожалуйста номер из списка")
            continue

        if user_choice == 1:
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
            for val in _list_books.values():
                if val.title == title and val.author == author and val.year == year:
                    print(f"Такая книга уже есть в библиотеке под номером {val.id}")
                    break
            else:
                book = Book(title, author, year)
                _list_books[book.id] = book
                print(_list_books)
                _id += 1

        elif user_choice == 2:
            pass
        elif user_choice == 3:
            pass
        elif user_choice == 4:
            show_all_book()
        elif user_choice == 5:
            pass
        elif user_choice == 0:
            exit()

# title = str(input("Введите название: "))
# if not title:
#     print("Название книги не может быть пустым"
#           "повторите ввод ")
#     continue
# author = str(input("введите автора"))
# if not author:
#     print("Название книги не может быть пустым"
#           "повторите ввод ")
#     continue
# try:
#     year = int(input("введите год"))
# except ValueError:
#     pass
# book = Book(title, author, year)
# _list_books[book.id] = book
# print(_list_books)
# _id += 1


main()

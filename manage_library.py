_id = 1  # счетчик будет увеличиваться в функции вызова создания объекта модели
_list_books = {}
_valid_status = ["в наличии", "выдана", ]


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.aythor = author
        self.year = year
        self.id = _id
        self.status = "в наличии"

    def change_status(self, status: str) -> None:
        if status in _valid_status:
            self.status = status
        else:
            raise ValueError(f"Статус {status} запрещен")


def find_book(title: str | None = None, author: str | None = None, year: int | None = None) -> list[cls]:
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
    for book in _list_books.values():
        print(f"Ниже представлены все книги в нашей библиотеке:"
              f"инедтификатор - {book.id}"
              f"Название книги - {book.title}"
              f"Автор книги - {book.author}"
              f"Год публикации - {book.year}"
              f"Наличие в библиотеке - {book.status}")

def main():
    global _id
    while True:
        title = str(input("введите название"))
        author = str(input("введите автора"))
        year = int(input("введите год"))

        book = Book(title, author, year)
        _list_books[book.id] = book
        print(_list_books)
        _id += 1


main()

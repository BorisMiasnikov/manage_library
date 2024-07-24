from functions_for_main import _create_library, _create_book, _delete_book, _find_library_book, \
    _chenge_status_library_book, _read_json, _get_new_book_data
from class_library_book import Book, Library


def main(value):
    try:
        _create_library(value)
    except FileNotFoundError:
        print("Давайте создадим новую библиотеку!")

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

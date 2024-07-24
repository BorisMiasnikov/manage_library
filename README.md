### Консольное приложение, система управления библиотекой

Для запуска приложения, скачайте файлы из репозитория на свой компьтер.

Перейдя в консоли в папку с файлом, выполните команду (на Windows) `python manage_library.py` далее следуйте инструкциям, выведенным в консоли

Вид инструкций:

    Выберите действия:
    Добавить книгу - введите 1
    Удалить книгу - введите 2
    Найти книгу - введите 3
    Показать все книги в библиотеке - введите 4
    Изменить статус книги - введите 5
    Для выхода введите 0


Приложение позволяет вести учет книгам, находящимся в библиотеке. Предполагается что для хранения книг, вводят:

Название - строковое значение

Автора - строковое значение

Год - целочисленное значение

По умолчанию книге присваивается идентификационный номер и статус `"в наличие"`

Статус книги можно изменить методом `_change_status` в классе книги (`Book`), книга может иметь два статуса, `выдана` и `в наличии`

Все книги в библиотеке записываются в JSON-файл, по умолчанию названный `Library`. Благодаря этому, после закрытия
приложнеия, данные о книгах в библиотеке не теряются и при следующем запуске приложения, все книги из предыдущего сеанса
будут доступны, и новые будут записаны и сохранены со следующим порядковым номером идентификатора.

Структура данных в JSON-файле выглядит следующим образом:

    [
        {
            "id": 1,
            "title": "1984",
            "author": "Джордж Оруэлл",
            "year": 1949,
            "status": "в наличии"
        },
        {
            "id": 2,
            "title": "Меч Предназначения",
            "author": "Сапковский Анджей",
            "year": 1992,
            "status": "выдана"
        },
        {
            ...
        },
        ...
    ]

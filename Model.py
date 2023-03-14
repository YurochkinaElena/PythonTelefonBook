import json
import controller


def read():
    try:
        with open('notes.json', 'r', encoding="utf-8") as data:
            book = json.loads(data.read())
        return book
    except:
        return []


def save(book):
    with open('notes.json', 'w', encoding="utf-8") as data:
        json.dump(book, data, indent=4, ensure_ascii=False)


def create_contact(book):
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    num_tel = input("Введите телефон: ")
    contact = {"First_name": first_name, "Last_name": last_name,
               "Patronymic": patronymic, "Telefon": num_tel}
    # book = controller.book
    book.append(contact)
    print('\nКонтакт создан')
    save(book)


def update_contact(book):
    return


def del_contact(book):
    return

# def sort(book):

import json
import controller

def read():
    try:
        with open('notes.json') as data:
            book = json.loads(data.read())
        return book
    except:
        return []

def save(book):
    with open('notes.json', 'w') as data:
        json.dump(book, data, indent=4)

def create_contact(book):
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    o_name = input("Введите отчество: ")
    num_tel = input("Введите телефон: ")
    contact = [first_name, last_name, o_name, num_tel]
    book.append(contact)
    print('\nКонтакт создан')
    save(book)

def update_contact(book):
    return

def del_contact(book):
    return

# def sort(book):
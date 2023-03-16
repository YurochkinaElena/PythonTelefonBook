import json
import controller
import View

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
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    num_tel = input("Введите телефон: ")
    contact = {"Last_name": last_name, "First_name": first_name, "Patronymic": patronymic, "Telefon": num_tel}
    # book = controller.book
    book.append(contact)
    print('\nКонтакт создан')
    save(book)


def update_contact(book):
    return


def del_contact(book):
    View.view(book)
    num_contact = int(input('Какой номер контакта удалить?: '))
    book.pop(num_contact-1)       
    print('\nКонтакт удален')
    save(book)

        
          










    #     print('\nКонтакт удален')
    # save(book)
    # line = ' '.join(contact) + '\n'
    #             data.write(line)
    
    #
    #     data.wrire()

   

# def sort(book):

# def delete_contact(file_name):
#   contact_list = read_file_to_list(file_name)
#     number_to_change = search_to_modify(contact_list)
#     contact_list.remove(number_to_change)
#     with open(file_name, 'w', encoding='utf-8') as file:
#         for contact in contact_list:
#             line = ' '.join(contact) + '\n'
#             file.write(line)

# def delete_contact_str_ru(book):
#     repl = delete_contact_ru(book['str'])
#     " != != '':
#         with open(file_book_ru["str"], "r", encoding="utf_8") as s:
#             allfile = s.read()
#         allfile = allfile.replace((repl+'\n'), ")
#         with open(file_book_ru['str'], "w", encoding="utf_8") as s:
#             s.write(allfile)
#         init_dict_ru(book, 'str')

# def delete(contacts):
#     print("Введите контакт: ")
#     name = input('> ')
#     for contact in contacts:
#         if contact['name'] == name:
#             print("Вы хотите удалить контакт %s (yes/no)?: " % name )
#             name_del = input('> ')
#             if name_del == 'yes':
#                contacts.remove(contact)
#                print("Вы удалили контакт %s " % name)
""" Дополнить телефонный справочник возможностью изменения
и удаления данных. Пользователь также может ввести имя или фамилию,
и Вы должны реализовать функционал для изменения и удаления данных. """

import os

os.system("cls")


def enter_first_name():
    return input("Введите имя абонента: ").title()


def enter_second_name():
    return input("Введите фамилию абонента: ").title()


def enter_family_name():
    return input("Введите отчество абонента: ").title()


def enter_phone_number():
    return input("Введите номер телефона: ")


def enter_address_number():
    return input("Введите адрес абонента: ").title()


def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address_number()
    with open("book.txt", "a", encoding="utf-8") as file:
        file.write(f"{name} {surname} {family} | {number} | {address}\n\n")


def print_data():
    with open("book.txt", "r", encoding="utf-8") as file:
        print(f"\n{file.read()}")


def search_line():
    print(
        "Выберите вариант поиска:\n"
        "1. Имя\n"
        "2. Фамилия\n"
        "3. Отчество\n"
        "4. Телефон\n"
        "5. Адрес"
    )
    index = int(input("Введите вариант: ")) - 1
    searched = input("Введите поисковые данные: ").title()
    with open("book.txt", "r", encoding="utf-8") as file:
        data = file.read().strip().split("\n\n")
        for item in data:
            new_item = item.replace("\n", " ").split()
            if searched in new_item[index]:
                print()
                print(item, end="\n\n")


def edit_data():
    with open("book.txt", "r", encoding="utf-8") as file:
        data = file.read()
        index_edit_data = int(input("Введите номер строки для редактирования: ")) - 1
        book_lines = data.split("\n")
        edit_book_lines = book_lines[index_edit_data]
        elements = edit_book_lines.split()
        name = input("Введите имя абонента: ")
        second_name = input("Введите фамилию абонента: ")
        family_name = input("Введите отчество абонента: ")
        number = input("Введите номер абонента: ")
        address = input("Введите адресс абонента: ")
        if len(name) == 0:
            name = elements[0]
        if len(second_name) == 0:
            second_name = elements[1]
        if len(family_name) == 0:
            family_name = elements[2]
        if len(number) == 0:
            number = elements[4]
        if len(address) == 0:
            address = elements[6]
        edited_line = f"{name} {second_name} {family_name} | {number} | {address}"
        book_lines[index_edit_data] = edited_line
        print(f"Запись ({edit_book_lines}) изменена на ({edited_line})\n")
        with open("book.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(book_lines))


def delete_data():
    with open("book.txt", "r", encoding="utf-8") as file:
        data = file.read()
        index_delete_data = int(input("Введите номер строки для удаления: ")) - 1
        book_lines = data.split("\n")
        delete_book_lines = book_lines[index_delete_data]
        book_lines.pop(index_delete_data)
        print(f"Удалена запись {delete_book_lines}\n")
        with open("book.txt", "w", encoding="utf-8") as file:
            file.write("\n".join(book_lines))


def interface():
    cmd = 0
    while cmd != "6":
        print(
            "Выберите действие: \n"
            "1. Добавить данные контакта\n"
            "2. Вывести все данные контакта\n"
            "3. Поиск данных контакта\n"
            "4. Изменение данных контакта\n"
            "5. Удаление данных контакта\n"
            "6. Выход\n"
        )
        cmd = input("Введите действие: ")
        while cmd not in ("1", "2", "3", "4", "5", "6"):
            print("Неккоректный ввод")
            cmd = input("Введите действие: ")
        match cmd:
            case "1":
                enter_data()
            case "2":
                print_data()
            case "3":
                search_line()
            case "4":
                edit_data()
            case "5":
                delete_data()
            case "6":
                print("Досвидания!")


interface()

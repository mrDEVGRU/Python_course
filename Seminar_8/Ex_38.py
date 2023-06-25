import os


def show_contacts(file_name):
    os.system("CLS")
    print("\nid | Surname | Name | Phone number")

    with open(file_name, "r") as file:
        data = file.readlines()

        for contact in data:
            print(contact, end="")

    input("\npress any key")


def add_contact(file_name):
    os.system("CLS")

    with open(file_name, "r") as file:
        contact = file.read()
    num = len(contact.split("\n"))
    with open(file_name, "a") as file:
        surname = input("Input a surname of contact: ")
        name = input("Input a name of contact: ")
        phone_number = input("Input a phone number of contact: ")

        file.write(f"{num} | {surname} | {name} | {phone_number}\n")

    input("\nContact was successfully added. Press any key for return")


def search_contact(file_name):
    os.system("CLS")
    target = input("Input a name of contact for searching: ")

    with open(file_name, "r") as file:
        contacts = file.readlines()

        for contact in contacts:
            if target in contact:
                print(contact)
                break
        else:
            print("there is no contacts with this name")

    input("\npress any key")


def edit_contacts(file_name):
    os.system("CLS")
    print("\nid | Surname | Name | Phone number")

    with open(file_name, "r") as file:
        contacts = file.read()
    print(contacts + "\n")

    index_delete_data = int(input("Input a number string for edit: ")) - 1
    contacts_lines = contacts.split("\n")
    edit_contacts_lines = contacts_lines[index_delete_data]
    elements = edit_contacts_lines.split(" | ")
    surname = input("Input surname: ")
    name = input("Input name: ")
    phone = input("Input phone number: ")
    num = elements[0]
    if len(surname) == 0:
        surname = elements[1]
    if len(name) == 0:
        name = elements[2]
    if len(phone) == 0:
        phone = elements[3]
    edited_line = f"{num} | {surname} | {name} | {phone}"
    contacts_lines[index_delete_data] = edited_line

    with open(file_name, "w") as file:
        file.write("\n".join(contacts_lines))

    input("\npress any key")


def delete_contacts(file_name):
    os.system("CLS")
    print("\nid | Surname | Name | Phone number")

    with open(file_name, "r") as file:
        contacts = file.read()
        print(contacts + "\n")

    index_delete_data = int(input("Input a number string for remove: ")) - 1
    contacts_lines = contacts.split("\n")
    del_contacts_lines = contacts_lines[index_delete_data]
    contacts_lines.pop(index_delete_data)

    with open(file_name, "w") as data:
        data.write("\n".join(contacts_lines))

    input("\npress any key")


def drawing():
    print("1 - show contacts")
    print("2 - add contacts")
    print("3 - search contacts")
    print("4 - edit contacts")
    print("5 - delete contacts")
    print("0 - exit")


def main(file_name):
    while True:
        os.system("CLS")
        drawing()
        user_choice = int(input("Input a number from 0 to 5: "))

        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contact(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4:
            edit_contacts(file_name)
        elif user_choice == 5:
            delete_contacts(file_name)
        elif user_choice == 0:
            print("Have a nice day")
            return


main("ContactsBook.txt")

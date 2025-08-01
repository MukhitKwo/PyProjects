
import sys
import os

todoList = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_list():

    clear()

    while True:

        todo = input("TODO: ")

        if todo == "e":
            break

        todoList.append(todo)


def show_list():

    clear()

    n = 0

    for todo in todoList:
        n += 1
        print(f"{n} - {todo}")


def remove_list():

    clear()
    show_list()

    while True:

        rem = input("Remove: ")

        if rem == "e":
            break

        todoList.pop(int(rem)-1)


while True:

    print("TODO LIST")
    print("a - add todo")
    print("s - show todo list")
    print("r - remove todo")
    print("e - exit")

    option = input("Option: ")[0]

    if option == "a":
        add_list()
    elif option == "s":
        show_list()
    elif option == "r":
        remove_list()
    elif option == "e":
        sys.exit()
    else:
        print("Option non-existent")

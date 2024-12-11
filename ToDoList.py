"""
Emanuel Toscano
12/6/24
To Do List project
This program allows to create your own to do list
Period 5
"""
#variables
ToDoList = [] #this is the list to hold our to do items

#functions
def add_item(item):
    """
    add_item adds an item to the end of the ToDoList
    :param item: item - a string representing a to do list item
    :return: nothing is returned
    """
    ToDoList.append(item)
    print_list()
#This function allows you to remove items from your list
def remove_item():
    """
    remove_item allows you to remove an item from ToDoList
    :return: if there is nothing to be removed, it returns "There is no item to remove"

    """
    if len(ToDoList) < 1: #ToDoList is the variable that is your list, it holds all the things you need to do in it
        print("There is no item to remove")
        return
    for c in range(0, len(ToDoList)):
        print(str(c + 1) + ". " + ToDoList[c])
    choice = input("Which one do you want to remove?: ") #the variable choice is the number you input to remove an item from ToDoList
    if choice.isdigit():
        choice = int(choice) -1
        if int(choice) >= len(ToDoList) or int(choice) < 0:
            print("Invalid choice")
        else:
            ToDoList.pop(choice)
    else:
        print("Invalid choice")


def reset_list():
    """
    reset_list allows you to clear all the items from ToDoList
    :return: nothing is returned
    """
    list.clear(ToDoList)

def print_list():
    """
    print_list prints out ToDoList but in chronological order and the numbers next to your item, also help in removing items from the list
    :return: nothing is returned
    """
    for c in range (0, len(ToDoList)):
        print(str(c + 1) + ". " + ToDoList[c])#The items in the ToDoList are printed out in order numerically


def show_menu():
    """
    show_menu prints out the menu when you start the code and gives you options to add an item, remove an item, clear the list, to display the list or to end the code
    Certain numbers are pressed to do these functions in the code
    :return: nothing is returned
    """
    while True:
        print("Add a new task to the To-Do list by pressing 1. ")
        print("Remove a task by selecting it's number from the list by pressing 2.")
        print("Display all tasks in the list by pressing 3. ")
        print("Clear all tasks and reset the list by pressing 4. ")
        print("Press 'q' to quit.")
        choice = input()
        if choice == "1":
            c = input("Add a new task: ")
            add_item(c)
        elif choice == "2":
            remove_item()
            print_list()
        elif choice == "3":
            print(print_list())
        elif choice == "4":
            reset_list()
        elif choice == 'q':
            print("Thank you, bye!")
            break
        else:
            print("Invalid input. Please try again.")

#Main code
print(show_menu())
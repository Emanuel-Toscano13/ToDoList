# This is how you create a list
myList = ["red", "orange", "blue"]
# Print the list
print(myList)
# Access individual items from the list using the index
print(myList[1])
# add an item to the list
myList.append("green")
print(myList)
# this will remove the 2nd item in the list
myList.pop(1)
#how to make amenu
#repeat until q is pressed
while True:
    print("Press 1 for fun")
    print("Press 2 for work")
    print("Press 3 for quit")
    choice = input()
    if choice == "1":
        print("You chose fun")
    elif choice == "2":
        print("You chose work")
    elif choice == "3":
        print("Bye!!")
        break
    else:
        print("Invalid choice")


list2 = ["a1", "a2", "a3", "a4", "a5"]

for c in range(0, len(list2)):
    print(str(c+1) + ". " + list2[c] )

while True:
    choice = input("Which one to remove or q to quit?")
    if choice == "q":
        break
    if choice.isdigit():
        choice = int(choice) - 1
        if int(choice) >= len(list2) or int(choice) < 0:
            print("Invalid choice")
        else:
            list2.pop(choice)
    else:
        print("Invalid choice")


print(list2)

from time import sleep
from random import randint




#counter = 0
def menu():
    while (True):
        print("MENU\n_______________\n1. Dog details\n2. Friends\n3. N azzeret\n")
    #######################################################
        choose=input("Choose a number ")
        if (choose == "1"):
            dog()
    #######################################################
        elif (choose == "2"):
            friends()

    #######################################################
        elif (choose == "3"):
            azzeret()

    #######################################################
        else:
            print("Choose 1-3 only")

        exit = input("Do you want to exit? y/n ")

        if (exit == "y"):
            print("\nBye bye")
            break

def dog():
    name = input("Enter name of your dog \n")
    age = int(input("Enter age of your dog \n"))
    print("Dog's name: " + name + "\nDog's age: " + str(age))


def friends():
    name_list = []
    for i in range(5):
        name_list.append(input("Enter name of friend "))
    name_new=input("Enter new name ")
    if(name_new in name_list):
        print(name_new + " is inside of the list\n")
    else:
        print(name_new + " isnt inside of the list\n")




def azzeret():
    num = int(input("Enter a number \n"))
    sum = 1
    for i in range(1, num + 1):
        sum = i * sum

    print(str(num) + "! = " + str(sum))

menu()
dog()
friends()
azzeret()

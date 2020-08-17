from time import sleep
from random import randint
counter=0
while(True):
    print("MENU\n_______________\n1. Printing 100 numbers\n2. Check fibo\n3. Randit numbers until we get 12 or we cout 12 times\n")
#######################################################
    choose=input("Choose a number ")
    if(choose=="1"):
        for i in range(1,101):
            print(i)
    #######################################################
    elif(choose=="2"):
#       fib = [1, 2, 3, 5, 8, 13, 21]
        fib = []
        num = input("Enter how many numbers do you want (more than 2)\n")
        for i in range(0, int(num)):
            fib.append(int(input("Enter a number ")))
        print(fib)
        print("You entered " + num + " numbers...\nChecking fibo...")
        sleep(2)
        boolean = "True"
        for i in range(2, int(num)):
            if fib[i] != fib[i - 1] + fib[i - 2]:
                boolean = "False"
                break
        if (boolean == "True"):
            print("Yes, fibonacci recursion\n\n")
        else:
            print("No fibonacci recursion\n\n")
            sleep(2)
    #######################################################
    elif (choose == "3"):
        counter=1
        num=randint(1,12)
        while(num!=12 and counter<11):
            print("Counter= " + str(counter) + "   num= " + str(num))
            counter=counter+1
            num=randint(1,12)




    #######################################################
    else:
        print("Choose 1-3 only")

    exit=input("Do you want to exit? y/n ")

    if(exit=="y"):
        print("Bye bye")
        break




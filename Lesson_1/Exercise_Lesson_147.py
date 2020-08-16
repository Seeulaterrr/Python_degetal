#Cube
from random import randint
from time import sleep
money=int(input("How much money do you have? "))
print("You have " + str(money//3) + " games\n")
games=money//3
sum=0
for i in range(games):
    print("Game number " + str(i+1) +":\n")
    sleep(2)
    cube1=randint(1,6)
    cube2=randint(1,6)

    print("Cube1: " + str(cube1) + "\nCube2: " + str(cube2) + "\n_____________")
    if(cube1==cube2):
        if(cube1==6):
            sum=sum+1000
        else:
            sum=sum+100
    elif(cube2==2):
        sum=sum+40
    elif(cube1==1):
        sum=sum+20
print("You win " + str(sum) + " dollar")



#Create 2 variables: string of your full name, another
#string of your mail. Create variable of your age (integer)
#Print your name from the end to the beginning and print it
#only with age*3
#Check if your full name is stored inside this ful
#string "I love you, Julya Petrov"
#
#
name=input("Enter your full name ")
mail=input("Enter your e-mail ")
age=int(input("Enter your age "))
#age=int(age)
print("Your full name from the end to the beginning is " + name[::-1] + "\nYour age*3 is: " + str(age*3))
print(name in "I love you, Julya Petrov")
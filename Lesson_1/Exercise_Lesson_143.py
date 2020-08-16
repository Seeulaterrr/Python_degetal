#Write a program that will show the menu:
#1. Enter number and ** it by 3
#2. Insert 4 IP to list and print it
#3. Insert 4 entries to DNS_Dictionary and print it
#4. Check if a string is Polindrom
#
#If the user won't choose 1-4, you will tell him to insert 1-4 only
#


print("MENU: \n1. Enter number and ** it by 3\n2. Insert 4 IP to list and print it\n3. Insert 4 entries to DNS_Dictionary and print it\n4. Check if a string is Polindrom")
N=input("Choose a number 1-4 ")
if (N=="1"):
    print("New number = " + str(int(input("Enter your number "))**3))
elif(N=="2"):
    my_list=[]
    my_list.append(input("Enter IP "))
    my_list.append(input("Enter IP "))
    my_list.append(input("Enter IP "))
    my_list.append(input("Enter IP "))
    print("My list: " + str(my_list))
elif(N=="3"):
    DNS_Dictionary={}
    DNS_Dictionary.update({input("Enter URL of "):input("Enter IP ")})
    DNS_Dictionary.update({input("Enter URL of "): input("Enter IP ")})
    DNS_Dictionary.update({input("Enter URL of "): input("Enter IP ")})
    DNS_Dictionary.update({input("Enter URL of "): input("Enter IP ")})
    print("My DNS Dictionary:\n" + str(DNS_Dictionary))
elif(N=="4"):
    My_string=input("Enter a string ")
    My_string1=My_string[::-1]
    if My_string==My_string1:
        print("A string <" + My_string + "> is polindrom")
    else:
        print("A string <" + My_string + "> is not polindrom")
else:
    print("Enter 1-4 only")

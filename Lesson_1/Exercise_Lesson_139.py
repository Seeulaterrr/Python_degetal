#Create a list with 4 details about you: name, age,
#mail, phone and print
#
#Create another list with 3 IP and add 3 more IP,
#pop the 3-rd IP and print how many IP do we have
#and print them

private=["Julya", "21", "Julya@gmail.com", "01234567"]
print("Name: " + private[0] + "\nAge: " + private[1] + "\nE-mail: " + private[2] + "\nPhone: " + private[3])
ip_list=["1.1.1.1", "2.2.2.2"]
print("My IP list: \n" + str(ip_list))
ip_list.append("3.3.3.3")
ip_list.append("4.4.4.4")
ip_list.append("5.5.5.5")
print("\nMy new IP list: \n" + str(ip_list))
ip_list.pop(3)
print("\nWe have " + str(len(ip_list)) + " IP in our list: \n" + str(ip_list))


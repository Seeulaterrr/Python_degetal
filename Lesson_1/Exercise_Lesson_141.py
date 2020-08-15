#Create a dictionary with 5 names and money,
#summ money of the first and last names, print the summ
#add a new name with the summ of the money
#print the number of entries and check if
#"Luba" is inside

my_dic={"Alla":30, "Sveta":16, "Alex":48,"Anton":0, "Luba":75}
print("The summ is: " + str(my_dic["Alla"]+my_dic["Luba"]))
my_dic["Julya"]=int(my_dic["Alla"]+my_dic["Luba"])
print(my_dic)
print("Number of entries: " + str(len(my_dic)))
print("Luba" in my_dic)
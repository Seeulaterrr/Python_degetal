print("Now we will calculate your marketing: \nPrices:\n----------------\nTomato - 3 Nis\nCucumber - 2 NIS\nKola - 5 Nis\nChiken - 20 Nis ")
tomato=int(input("How many tomatos do u want? "))
cucamber=int(input("How many cucamber do u want? "))
cola=int(input("How many cola do u want? "))
chicken=int(input("How many chicken do u want? "))

#print("SUMM OF YOUR ORDER: \nTomates - " + str(tomato) + "\nCucamber - " + str(cucamber) + "\nCola - " + str(cola) + "\nChicken - " + str(chicken) + "\nSUMMM:  " + str(summ))
print("SUMM OF YOUR ORDER: \nTomates - " + str(tomato) + "x" + str(3) + "   =  " + str(3*tomato) + " NIS")
print("\nCucambers - " + str(cucamber) + "x" + str(2) + "   =  " + str(2*cucamber) + " NIS")
print("\nCola - " + str(cucamber) + "x" + str(5) + "   =  " + str(5*cola) + " NIS")
print("\nChicken - " + str(cucamber) + "x" + str(20) + "   =  " + str(20*chicken) + " NIS")
summ=3*tomato+2*cucamber+5*cola+20*chicken
print("\nYou have to pay " + str(summ) + " Nis without tax")
print("\nYou have to pay " + str("%.2f" %(summ*1.17) + " Nis with tax"))
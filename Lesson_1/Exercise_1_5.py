#This program accepts an integer (n) and computes
#the value of n+nn+nnn
#
n=input("Enter n (integer) ")
n=int(n)
print("n=" + str(n) + "\nValue= " + str(n+n*10+n+n*100+n*10+n))

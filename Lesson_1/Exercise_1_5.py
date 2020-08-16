#This program accepts an integer (n) and computes
#the value of n+nn+nnn
#
n=input("Enter n (integer) ")
n=int(n)
print("n=" + str(n) + "\nValue= " + str(n+n*10+n+n*100+n*10+n))

#Write a program to find whether a given number
# (accept from the user) is even or odd, print out
# an appropriate message to the user.

m=input("Enter m (integer) ")
k=int(m)//2
if (k==1):
    print("m=" + str(m) + " odd")
else:
    print("m=" + str(m) + " even")
n=int(input("enter The positive value "))
fact=1
if n==0:
    print(" factorial is\t ",fact)
else:
    i=n
    while (i>=1):
        fact=fact*i
        i=i-1
print("Factorial of",n,"is\t",fact)
    

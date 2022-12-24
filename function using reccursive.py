#factorial with recursive Function:

def fact(x:int):
    if (x==1) or (x==0):
        return 1
    else:
        return (x*fact(x-1))
    #print(x)
n=int(input("Enter any no."))
fact(n)
print(fact(n))

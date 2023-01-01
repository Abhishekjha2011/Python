#sum natural no. with recursive Function:

def sum(x:int):
    if (x!=0):
        return (x+sum(x-1))
    else:
        return 0
n=int(input("Enter any no."))
res=sum(n)
print(res)

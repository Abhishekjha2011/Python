
#wap to find whether no. is armstrong or not?
n=int(input("Enter the N no."))
i=len(str(n))
sum=0
e=n
t=0
while(n!=0):
    t=n%10
    f=t**i
    sum=sum+f
    n=n//10
    if e==sum:
        print("Number is armstrong",sum)
else:
    print("Number is not armstrong",sum)
    

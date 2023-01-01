r=int(input("Enter the Number of row"))
c=int(input("Enter the NUmber of Column"))
for i in range(1,r):
    for j in range(r-1,i-1,-1):
        print(j, end='')
    print('\n')





r=int(input("Enter the Number of row"))
c=int(input("Enter the NUmber of Column"))
for i in range(1,r):
    for j in range(1,i+1):
        print(i, end='')
    print('\n')


r=int(input("Enter the Number"))

for i in range(r,0,-1):
    for j in range(1,i+1):
        print(i, end='')
    print('\n')


r=int(input("Enter the Number"))
k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k, end='')
        k=k+1
    print('\n')

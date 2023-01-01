class compute:
    def area(self,x=None,y=None):
        if x!=None and y!=None:
            return x*y
        elif x!=None:
            return x*x
        else:
            return 0
obj=compute()
a=obj.area()
b=obj.area(6)
c=obj.area(2,8)
print(a)
print(b)
print(c)

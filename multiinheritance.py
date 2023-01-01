# Multiple Inheritance

class calculation1:
    def summation(self,a,b):
        return a+b;
class calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(calculation1,calculation2):
    def Divided(self,a,b):
        return a/b;
d=Derived()
print(d.summation(10,200))
print(d.Multiplication(10,200))
print(d.Divided(10,200))
c=calculation1
b=calculation2
#
print(issubclass(Derived,calculation2))
print(issubclass(calculation1,calculation2))
#The Instance(obj,Class)Method:
print(isinstance(d,Derived))
print(isinstance(c,Derived))
print(isinstance(b,calculation1))


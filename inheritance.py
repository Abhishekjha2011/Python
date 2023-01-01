#inheritence:

#class Animal:
   # def speak(self):
        #print("Animal Speaking")
#class dog(Animal):
   # def bark(self):
       # print("dog barking")
#d=dog()
#d.bark()
#d.speak()


# Double inheritence:
class Animal:
    def speak(self):
        print("Animal Speaking")
class dog(Animal):
    def bark(self):
        print("dog barking")
class dogchild(dog):
    def eat(self):
        print("Eating bread..")
d=dogchild()
d.bark()
d.speak()
d.eat()

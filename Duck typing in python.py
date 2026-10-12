# Duck Typing :

#-->It is the concept in python where the type of class of an object is less important than the methods or properties it has.

#--> In duck types it checks as behaviour (methods/ attributes) noit the actual type of object.


#Example-->

class dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

class Duck:
    def sound(self):
        print("Quark")

class Animal(x):
    x.sound()

    for i in (Dog(), Cat(), Duck()):
        Animal(i)

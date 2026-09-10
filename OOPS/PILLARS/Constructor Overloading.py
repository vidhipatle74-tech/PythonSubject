# Constructor overloading-->

#(1)--> Developing multiple  constructor in the same class with variation in argument list
#         is called constructor overloading.


#Syntax--> class Dim:
"""
   def __init__(self):
       print("constructor1")


   def __init__(self, a):
       print("constructor2")


   def __init__(self,a ,b):
       print("constructor3")


d = Dim(10, 20) 
"""


#=>>Constructor with variable number of arguments

#If we pass more than declared variable values to _ init_() it will
#Throw error to avoid this we use *args
"""
class Car1:
   def __init__(self,brand,model,price,*args):
       print(f'{brand} brand with {model} price is {price}')
       print(f'extra information are {args}')
      
c=Car1("kia","k7","Rs15lkh")
c1=Car1("kia","k7","Rs15lkh","white","2019 engine")
"""

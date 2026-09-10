#---------------------------------------------------------------------------------------------------------------
#(1)-->Store and Display Name
# Create a class Student
#Constructor should take name
#      Print the name
#      Your Task
#      Output: Rahul
#-----------------------------------------------------------------------------------------------
"""
class student:

    def __init__(self):
        print(f'Rahul')
s=student()
"""
# o/p--> Rahul

#---------------------------------------------------------------------------------------------
#(2)-->Store Two Values
#Create class Employee
 # Take name and salary
# Print both
# Output: Ravi 25000
#------------------------------------------------------------------------------------------
"""
class employee:

    name="vidhi"
    age=21

    def show_data(self):
        print(f'the name of the employe is {self.name}')
        print(f'the age of the employee is {self.age} ')
e=employee()
e.show_data()
"""
# o/p--> the name of the employe is vidhi
#             the age of the employee is 21 
#-----------------------------------------------------------------------------------------
#(3)-->Calculate Square
#          Constructor takes a number
#          Store square in variable
#          Print result
#Input: 5
# Output: 25
#--------------------------------------------------------------------------------------------
"""
class square:

    def __init__(self,num):
        self.square = num*num
        print(self.square)

s=square(5)
"""
#o/p--> 25
#----------------------------------------------------------------------------------------------  
#(4)-->Create class Laptop
# Store:
#          brand
#          price
#          RAM
#     Print like:
#     HP 50000 16GB
#-------------------------------------------------------------------------------------------
"""
class laptop:

    brand="Hp"
    price=50000
    ram="16gb"

    def data(self):
        print(f'The brand of the laptop is {self.brand}')
        print(f'The price of the laptop is {self.price}')
        print(f'The RAM of the laptop is {self.ram}')
l=laptop()
l.data()
"""
#o/p--> The brand of the laptop is Hp
#            The price of the laptop is 50000
#            The RAM of the laptop is 16gb




















 

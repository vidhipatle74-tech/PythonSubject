"""class data:
    def __init__(self):
        print("first class")
d=data()
data.__init__(d)
"""
"""
class vidhi:
    def __init__(self):
        print("afternoon")

    def __init__(self):
        print("evening")
v=vidhi()
"""
# calling instance method into the constructor:
"""
class car:
    def __init__(self):
        self.name="bmw"
        self.color="red"
        self.cost="1cr"

        print(f'My car name is {self.name}')
        print(f'My car color is {self.color}')
        print(f'My car cost is {self.cost}')
c=car()
 """

#(6)-->constructor + instance method without parameter

#calling one method into another method
"""
class car:
    def __init__(self):
        self.name="bmw"
        self.color="red"
        self.cost="1cr"
        self.show_data()

    def show_data(self):
        print(f'My car name is {self.name}')
        print(f'My car color is {self.color}')
        print(f'My car cost is {self.cost}')
c=car()
c.show_data()
"""
"""
class room3:
    def __init__(self,total_student,total_girls,total_boys,total_sub,*args):
        self.student=total_student
        self.girls=total_girls
        self.boys=total_boys
        self.sub=total_sub
        self.args=args
    def show(self,):
        print(f'The total student in class is {self.student}')
        print(f'the total girls in class is {self.girls}')
        print(f'the total boys in class is {self.boys}')
        print(f'the total subject in the class is {self.sub}')
        print(f'extra information {self.args}')
r=room3(100,50,50,8,"*",90)
r.show()
print()
"""
"""
class room3:
    def __init__(self,total_student,total_girls,total_boys,total_sub,**kwargs):
        self.student=total_student
        self.girls=total_girls
        self.boys=total_boys
        self.sub=total_sub
        self.kwargs=kwargs
    def show(self,):
        print(f'The total student in class is {self.student}')
        print(f'the total girls in class is {self.girls}')
        print(f'the total boys in class is {self.boys}')
        print(f'the total subject in the class is {self.sub}')
        print(f'extra information {self.kwargs}')
r=room3(100,50,50,8,a="*",b=90)
r.show()
print()
"""

class bank:

    def __init__(self):
        self.balance=0.0

    def deposite(self,amount):
        print(f'before deposite the total amount is {self.balance}')
        self.balance=self.balance+amount
        print(f'after deposite total amount is {self.balance}')

    def withdraw(self,amount):
        self.balance=self.balance-amount
        print(f'after withdraw the total amount is {self.balance}')
B=bank()
#b.balance=1000
bank.balance=10000
print(B.balance)   #0.0
B.deposite(5000)   #5000
B.withdraw(3000)        #2000

        
        
    
        
    

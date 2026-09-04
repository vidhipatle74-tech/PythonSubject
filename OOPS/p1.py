"""
class dog:
    def details(self,name,breed):
        self.name=name
        self.breed=breed
        self.display_details()

    def display_details(self):
        print(self.name)
        print(self.breed)
d=dog()
d.details('dora',12)
"""
#o/p--> dora
#              12
"""
class school:
    def classes(self,trainer,subject):
        self.trainer=trainer
        self.subject=subject
        self.office()
    def office(self):
        print(f'The trainer is {self.trainer}')
        print(f'The subject is {self.subject}')
s=school()
s.classes('prabhu sir ','python')
"""

#o/p--> The trainer is prabhu sir 
#             The subject is python

#1.Create a class Person
#Store name and age
#Display details
"""
class person:
    def data(self,name,age):
        self.name=name
        self.age=age
        self.details()

    def details(self):
        print(f'the name of the peron is {self.name}')
        print(f'the age of the person is {self.age}')
p=person()
p.data('vidhi',21)

#o/p-->the name of the peron is vidhi
#            the age of the person is 21
"""
#modification by using object-->
"""
p.name="dora"
p.details()
"""
#o/p;--> the name of the peron is dora
#              the age of the person is 21


class person:
    a=name
    b=age

    def details(self,name,age):
        print(f'the name is{person.name}')
        print(f'the age is {person.age}')
p=person()
print()
        
    
 



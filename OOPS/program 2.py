"""class Student:
    sub="SQL"   #classvariable
    def subject_name(self):
        print(f'subject name is {self.sub}')
s=Student()

#Modification by using Class Name
Student.sub="Python"
"""
"""
class employee:
    sal=7000
def data(self):

#modification uby using classname:

#(object part is recomended part)
    
employee.data="1000"
"""
#by using object
"""
class person:
    def name(self):
        self.name1="ram"
        self.age=21
        self.sal=7000
        self.data()

    def data(self):
        print(f'person name is {self.name1}')
        print(f'person age is {self.age}')
        print(f'person sal is {self.sal}')
a=person()
a.name()

"""
#by using class name 

class person:
    def name(self):
        self.name1="ram"
        self.age=21
        self.sal=7000
        person.data(a)

    def data(self):
        print(f'person name is {self.name1}')
        print(f'person age is {self.age}')
        print(f'person sal is {self.sal}')
a=person()
a.name()

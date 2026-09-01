#instance method-->"""
class Demo:
    def spam(self):
        print("welcome To All")

d=Demo()
d.spam()   #d.spam(d)
Demo.spam(d)
"""


"""
class Joy:
    def spam(self):
        print(self)
j=Joy()
print(j)
j.spam()

print()


class Joy:
    def spam(x):
        print(x)
j=Joy()
print(j)
j.spam()
"""

"""
class School:
    name="Pyspiders"  #class variable
    def Data(self):
        print("working")
        print("Accessing Class variable by useing Class name")
        print(http://School.name)
        print("Accessing Class variable by useing object")
        print(http://self.name)
        # print(name) #NameError:
s=School()
http://s.Data()
"""




#modification by using object-->

#way----->01
"""
class Student:
    sub="SQL"   #classvariable
    def subject_name(self):
        print(f'subject name is {self.sub}')
s=Student()
"""
#Modification by using Class Name

# Student.sub="Python"

#Modification by using Object
"""
s.sub="Python_and_Sql"
s.subject_name()
"""


#way--->02
"""
class Student:
    sub="SQL"   #classvariable
    def subject_name(self):
        print(f'subject name is {Student.sub}')
s=Student()
"""
#Modification by using Class Name
"""
Student.sub="Python"
"""
#Modification by useing Object
"""
 s.sub="Python_and_Sql"
s.subject_name()
"""


#Note :--->
"""
(1)-->
if we access class variable by useing self object
if we done Modification by useing class_Name and
object it will effected
"""
"""
(2)-->
if we access class variable by useing ClassName
if we done Modification by useing class_name it 
will effected but if we done Modification by useing
object it will won't effected.
"""
"""
#by using object

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
"""
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
"""

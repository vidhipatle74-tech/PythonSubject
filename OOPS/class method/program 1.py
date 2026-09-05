#Accessing class variable into class method--->
"""
class student:
    name="vidhi"
    sub="python"

    @classmethod
    def show_data(cls):
        print(f'the student name is {cls.name}')
        print(f'the subject name is {cls.sub}')
student.show_data()
"""
#o/p--> the student name is vidhi
#              the subject name is python

#Modification in class method  --->
#by using two way:
#                                (1)--> by using cls
#                               (2)--> by using classname

#(1)--> by using cls-->
"""
class student:
    name="vidhi"
    sub="python"

    @classmethod
    def show_data(cls):
       # print(f'the student name is {cls.name}')
      #  print(f'the subject name is {cls.sub}')

        cls.name="abhi"
        cls.sub="java"
        print(f'the student name is {cls.name}')
        print(f'the subject name is {cls.sub}')

student.show_data()
"""
#o/p--> the student name is vidhi
#             the subject name is python
#             the student name is abhi
#             the subject name is java

#(2)-->By using classname--->
"""
class student:
    name="vidhi"
    sub="python"

    @classmethod
    def show_data(cls):
       # print(f'the student name is {cls.name}')
      #  print(f'the subject name is {cls.sub}')

        student.name="abhi"
        student.sub="java"
        print(f'the student name is {student.name}')
        print(f'the subject name is {student.sub}')

student.show_data()
"""
#o/p--> the student name is abhi
#              the subject name is java

#ANOTHER WAY ==>>>
#by using cls-->

"""
class school:
    fees=50000

    @classmethod
    def data(cls):
        print(f'the total  fees is {cls.fees}')

    @classmethod
    def updated_data(cls):
        school.fees="70000"
        print(f'the updated school fees is {cls.fees}')
x=school()
x.data()
x.updated_data()
"""
#o/p--> the total  fees is 50000
#             the updated school fees is 70000

#by using classname-->
"""
class school:
    fees=50000

    @classmethod
    def data(cls):
        print(f'the total  fees is {school.fees}')

    @classmethod
    def updated_data(cls):
        cls.fees="70000"
        print(f'the updated school fees is {school.fees}')
x=school()
x.data()
x.updated_data()
"""
#o/p-->the total  fees is 50000
#           the updated school fees is 70000


# Class variable of we are not accessing in class method  and
# outside we are doing modification
# it will affect for both classname and object-->

#by using classname-->
"""
class person:
    name="ram"

    @classmethod
    def data(cls):
        print(f'the person name is {person.name}')
person.data()
person.name="vidhi"
print(person.name)
"""
#o/p--> the person name is ram
#            vidhi

#by using object-->
"""
class person:
    name="ram"

    @classmethod
    def data(cls):
        name="ram"
x=person()
print(f'the person name is {x.name}')
x.data()
x.data="vidhi"
print(x.data)
"""
#o/p--> the person name is ram
#            vidhi



# by using object--->
"""
class person:
    name = "ram"      

    @classmethod
    def data(cls):
        name="ram"
        print(f'the person name is {x.name}')
        x.data = "vidhi"
        print(f'the person name is {x.name}')
x = person()
print(x.data)
"""
#Modification using classname after accessing class variable inside the class method --->
#by classname-->
"""
class employee:
    Ename="john"

    @classmethod
    def data(cls):
        print(f'The employee name is {employee.Ename}')
employee.data()
employee.Ename="sanem"
print(f'The updated name of the employee is {employee.Ename}')
"""
#o/p--> The employee name is john
#            The updated name of the employee is sanem

#Modification using object after accessing the class variable inside the class method -->
#by object-->

class employee:
    Ename="john"

    @classmethod
    def show_data(cls):
        Ename="john"
        print(f'The name of the employee is {e.show_data}')

e=employee()
e.show_data()
print(f'The updated name of the employee is {e.show_data}')

#o/p--> The updated name of the employee is <bound method employee.show_data of <class '__main__.employee'>>

























    


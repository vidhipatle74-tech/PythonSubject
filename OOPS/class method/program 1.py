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

        cls.name="abhi"
        cls.sub="java"
        print(f'the student name is {student.name}')
        print(f'the subject name is {student.sub}')

student.show_data()
"""
#o/p--> the student name is abhi
#              the subject name is java

#ANOTHER WAY ==>>>
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


class school:
    fees=50000

    @classmethod
    def data(cls):
        print(f'the total  fees is {school.fees}')

    @classmethod
    def updated_data(cls):
        school.fees="70000"
        print(f'the updated school fees is {school.fees}')
x=school()
x.data()
x.updated_data()



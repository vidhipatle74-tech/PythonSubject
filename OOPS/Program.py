#oop's=>>
"""
class Student:                  #classname
    name="rock"          #class variable--> name , age , total_sub
    age=23
    total_sub=5
s=Student()             #object creation
"""
#direct we cant access class data outside it will show :-->name error
"""
print(name)
print(age)
print(total_sub)
"""

#How ro access class variable data outside-->

#(1)--> by using classname
#(2)--> by using object

#(1)by using classname-->
"""
print(f'the student name is {Student.name}')
print(f'the student age is {Student.age}')
print(f'the student total subject is {Student.total_sub}')
"""
#o/p--> the student name is rock
#             the student age is 23
#             the student total subject is 5


#(2) by using object-->



#internally all data is stores in  the form of dictionary

#ACCESS MODIFIER==>
"""
# A=10--> public
#-A=10--> protected
#_ _A=10-->private
"""


#doc string==>> discription of the class
# if we want complete information ==(help.student)
"""
class Student:                  
    name="rock"          
    age=23
    total_sub=5
s=Student()

print(Student.__dict__)
"""



class employe:

    age=21
    sal=20000
    
emp=employe()
emp1=employe()
"""
print(emp.age)   #21
print(emp.sal)    #20000
"""
#modification in main class:

employe.age=25
print(employe.age)
print(emp.sal)
print(emp1.sal)



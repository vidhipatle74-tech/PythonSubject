"""
class student:
    name="abc"       #class variable name
    def data(self):
         # accessing class variable into instance method
         print(student.name)
         
s=student()
s.data()
"""
#o/p--> abc

#modification classvariable into instance method.

#(1)--> by using classname:
"""
student.name="vidhi"
s.data()
"""
#o/p--> vidhi

#(2)--> by using object:
"""
s.name="jhon"
s.data()
"""
#o/p--> abc


#accessing class variable into instance mehtod using object-->

class student:
    name="hii"
    def data(self):
        print(s.name)
s.data
    

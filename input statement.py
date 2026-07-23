Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
>>> 
>>>       #INPUT AND OUTPUT STATEMENT:
>>> 
>>> #INPUT VALUE:---> It is a inbuilt method used to take input from the user
>>> 
>>> #SYNTAX:--->  Var= datatype(input('msg'))
>>> 
>>>   #EXAMPLE:--> a= num(input('enter num'))
>>> 
>>> #--> by default input will take string as input value
>>> #--> EVAL()-->> it is a in built function which is used to take input from the users , specially for collection datatype .
>>> 
>>> a=eval(input('enter int data'))
enter int data98
>>> a
98
>>> a=int(input('enter data'))
enter data678
>>> a
678
>>> b=float(input('enter data'))
enter data6.7
>>> a
678
>>> b
6.7
>>> b=complex(input('enter data'))
enter data67
b
(67+0j)
b=bool(input('enter data'))
enter data67
b
True
b=bool(input('enter data'))
enter data0
b
True
b=bool(input('enter data'))
enter data1
b
True
b=bool(input('enter data'))
enter dataTrue
B
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    B
NameError: name 'B' is not defined. Did you mean: 'b'?
b
True
b=bool(input('enter data'))
enter dataFalse
b
True



#PRINT STATEMENT:

#it is used to display output in python [on screen]

#SYNTAX:-->  Print(val1,val2.............,valn,end='\n',seperater='')

             # By default seperator will take space as value
             
             # By default it will take next line as value.
             


a=("hello")
b=("my")
c=("name")
d=("is")
e=("vidhi")
print(a,b,c, end='d', seperater='#')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(a,b,c, end='d', seperater='#')
TypeError: print() got an unexpected keyword argument 'seperater'
print(a,b,c, end='d', seperator='#')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(a,b,c, end='d', seperator='#')
TypeError: print() got an unexpected keyword argument 'seperator'
print(a,b,c, end='d', sep='#')
hello#my#named
print(a,b,c, end=(d), sep='#')
hello#my#nameis
print(a,b,c, end=(d,e), sep='#')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print(a,b,c, end=(d,e), sep='#')
TypeError: end must be None or a string, not tuple

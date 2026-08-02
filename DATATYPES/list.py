Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# how to create empty list in normal way
a=[]
a
[]

#how to create empty list using object

list()
[]

e=list()
e
[]
type(e)
<class 'list'>

#list data type is a ordered data type
s=[11,22,33,44,55]
s
[11, 22, 33, 44, 55]
s=["abc",123,"true",(5+6j),false]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s=["abc",123,"true",(5+6j),false]
NameError: name 'false' is not defined. Did you mean: 'False'?
s=["abc",123,True,(5+6j),False]
S
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    S
NameError: name 'S' is not defined. Did you mean: 's'?
s
['abc', 123, True, (5+6j), False]


#list data type it willa ccept duplicate value
x=[1,2,3,4,5,'a','b','c',]
len(x)
8

#in list data type each element seperated by comma
c=[123456]
c
[123456]

c=[1,2,3,4,5,6]
c
[1, 2, 3, 4, 5, 6]

#in list data type we can do indexing and slicing
e=[100,89.78,True,"welcome","walmart","goodluck",12]
e[-6]
89.78

e[6]
12

e[4]
'walmart'

e[90]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    e[90]
IndexError: list index out of range

e=[100,89.78,True,"welcome","walmart","goodluck",12]

e[4]=500
e
[100, 89.78, True, 'welcome', 500, 'goodluck', 12]
#SYNTAX: v_n[position]=value


e[2]=False
e
[100, 89.78, False, 'welcome', 500, 'goodluck', 12]

e
[100, 89.78, False, 'welcome', 500, 'goodluck', 12]
#it is mutable data type which give output in updated one #


dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'c', 'e', 's', 'x']
dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']











    #METHODS OF LIST


#HOW TO CREATE EMPTY LIST
x=[]
x
[]


#first will add single value data type
x.append(10)
x
[10]

x.append(45.23)
x
[10, 45.23]

x.append(1+2j)
x
[10, 45.23, (1+2j)]

x.append(False)
x
[10, 45.23, (1+2j), False]

#second part will add collection data type

x.append("python")
x
[10, 45.23, (1+2j), False, 'python']


x.append((23,900))
x
[10, 45.23, (1+2j), False, 'python', (23, 900)]

x.append([12,13,13,14])
x
[10, 45.23, (1+2j), False, 'python', (23, 900), [12, 13, 13, 14]]

x.append({500,900})
x
[10, 45.23, (1+2j), False, 'python', (23, 900), [12, 13, 13, 14], {900, 500}]
x.append({23:45})
x
[10, 45.23, (1+2j), False, 'python', (23, 900), [12, 13, 13, 14], {900, 500}, {23: 45}]


#append methods error

x.append()
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    x.append()
TypeError: list.append() takes exactly one argument (0 given)

x.append(11,13)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    x.append(11,13)
TypeError: list.append() takes exactly one argument (2 given)
x.append((11,13))
x
[10, 45.23, (1+2j), False, 'python', (23, 900), [12, 13, 13, 14], {900, 500}, {23: 45}, (11, 13)]



 



#EXTEND()

s=[]
s
[]

s.append([100,200,300])
s
[[100, 200, 300]]


s.extend([100,200,300])
s
[[100, 200, 300], 100, 200, 300]
s.extend([{"a","b","c"})
         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
s
         
[[100, 200, 300], 100, 200, 300]
s.extend({"a","b","c"})
         
s
         
[[100, 200, 300], 100, 200, 300, 'b', 'c', 'a']



s=[[100, 200, 300], 100, 200, 300, 'a', 'b', 'c']
         
s.extend({555:999})
         
s
         
[[100, 200, 300], 100, 200, 300, 'a', 'b', 'c', 555]


s.append("Hello")
         
s
         
[[100, 200, 300], 100, 200, 300, 'a', 'b', 'c', 555, 'Hello']

s.extend("Hello")
         
s
         
[[100, 200, 300], 100, 200, 300, 'a', 'b', 'c', 555, 'Hello', 'H', 'e', 'l', 'l', 'o']



#append vs extend
         

z=[]
         
z
         
[]

z.append("python")
         
z
         
['python']

z.extend([900,1000])
         
z
         
['python', 900, 1000]

z.append([900,1000])
         
z
         
['python', 900, 1000, [900, 1000]]
z.append({1,2,3,4,5,6})
         
z
         
['python', 900, 1000, [900, 1000], {1, 2, 3, 4, 5, 6}]
>>> z.extend({12:45,78:45})
...          
>>> z
...          
['python', 900, 1000, [900, 1000], {1, 2, 3, 4, 5, 6}, 12, 78]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>>                        #INSERT METHOD
...          
>>> 
>>> 
>>>  #syntax:
...          
>>> 
>>>         #     v_n.insert(position,value)
...          
>>> 
>>> x=[10,20,30,40]
...          
>>> x
...          
[10, 20, 30, 40]
>>> 
>>> x.insert(0,100)
...          
>>> s
...          
[[100, 200, 300], 100, 200, 300, 'a', 'b', 'c', 555, 'Hello', 'H', 'e', 'l', 'l', 'o']

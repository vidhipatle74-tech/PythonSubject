Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


      #SET DATA TYPE():

# if we want to store unique element then we can go for set data type

#it is unordered data type

#it is mutable data type

#it will accepts only immutable data type ans single value datatype
#SYNTAX:   ----> {ele1,ele2,elel3........}

#if you want to create empty set , then you need to use object (  set()  )
#here we cannot create empty set normally



a={2,3}
a
{2, 3}
type(a)
<class 'set'>

#if we pass mutable data type it will throw unhashable type of error
#it will accepts only immutable and single valued data typoe

e={False,2,2.2,(1,2),'hi',(3+4j)}

len(e)
6

e={0,False,True,1,8,8,12}
len(e)
4

dir(17)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']





#ADDING METHOD AND UPDATE METHOD

ADDING METHOD:
    
SyntaxError: invalid syntax



#ADDING METHOD:

a={}
a.add(10)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.add(10)
AttributeError: 'dict' object has no attribute 'add'
#beacuse empty braces acts like a dictionart data type

b={10}
b
{10}

b={False}
b
{False}
b=(False)
b
False
b.add(10)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b.add(10)
AttributeError: 'bool' object has no attribute 'add'





b=(10)





a={1123,476,89678,9895787,9875857}
a.remove(476)
a
{9875857, 1123, 9895787, 89678}
a={1123,476,89678,9895787,9875857}
a.remove(666)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.remove(666)
KeyError: 666
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a={}
>>> 
>>> 
>>> a={12,34,34,24,56,12,89}
>>> a.symmetric_differene+ce()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    a.symmetric_differene+ce()
AttributeError: 'set' object has no attribute 'symmetric_differene'. Did you mean: 'symmetric_difference'?
>>> 
>>> 

>>> 
>>> 
>>> 

... 
>>> 

... 
>>> 

>>> 

>>> e={"chat","bat","snap","mat","hit"}

Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#First day class
#What is the meaning of keyword---->??
#How to get all 35 keywords in group format??
help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

#how to get all 35 keywords in list format??
#step1-->
import keyword

#step2-->
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#we can't assing any value to the keywords
not="100"
SyntaxError: invalid syntax
#how to check whether the given keyword is valid or not-->??
#here we need to follow thw syntax
#import keyword
#keyword.iskeyword


#if the given keyword is valid your output should be true.

#if the given keyword is invalid your output should be false.





import keyword
keyword.iskeyword
<built-in method __contains__ of frozenset object at 0x0000024FD3E4EA40>




KeyboardInterrupt
KeyboardInterrupt
<class 'KeyboardInterrupt'>




import keyword
keyword.iskeyword('python')
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: multiple statements found while compiling a single statement
SyntaxError: invalid syntax











import keyword
keyword.iskeyword('python')
False


import keyword
keyword.iskeyword('else')
True



import keyword
keyword.iskeyword('if')
True


#variable rule:

#in the place of variable we can use alphabet (uppercase/ lower/ combination)
abc=100
abc
100

ABC="HII"
ABC
'HII'


AbAb=786
AbAb
786


# in the place of variable should not starts with the number but we can use number in between or last.
12abc=100
SyntaxError: invalid decimal literal

abc12=75
abc12
75

a1b2c3=875
a1b2c3
875


#in the place of variable we cant use special charcter except underscore(_)

first day="started"
SyntaxError: invalid syntax

@=89
SyntaxError: invalid syntax

hi_hello="hii"
hi_hello
'hii'


_=5654
_
5654


#in the place of variable we can use unlimites character.
#but according to rule we can pass 79 character.
#Rule_name---->PEP8  (one of the rule name P-python,E-enhancement,P-proposal,8-version)
#WHY WE ARE USING PEP8---(IF YOU WAN TO FOLLOW PROTOCOL  OR GUIDELINES ,THATS WHY WE USE THAT)



#How to assign multiple variable with multiple value---
a,b,c=10,20,30
c
30

>>> b
20
>>> 
>>> a
10
>>> 
>>> 
>>> x,y,z=1,2
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    x,y,z=1,2
ValueError: not enough values to unpack (expected 3, got 2)
>>> #Multiple variable with single value---
>>> 
>>> x=y=z=100
>>> y
100
>>> x
100
>>> z
100
>>> #[using assignment operator]
>>> 
>>> x,y=y,x
>>> 
>>> 
>>> a=900
>>> b="python"
>>> 
>>> a,b=b,a
>>> b
900
>>> a
'python'

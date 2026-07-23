Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#subtraction operation can't support string data type
'hiiiiiii'-'hii'
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    'hiiiiiii'-'hii'
TypeError: unsupported operand type(s) for -: 'str' and 'str'

#subtraction operation can't support dict data type
['khushi','vidhi']-['khushi','vidhi']
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    ['khushi','vidhi']-['khushi','vidhi']
TypeError: unsupported operand type(s) for -: 'list' and 'list'


('khushi','vidhi')-('khushi','vidhi')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ('khushi','vidhi')-('khushi','vidhi')
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
#subtraction operation can't support tuple to tuple data type


#subtraction operation can support set to set data type
-{45,18,7}-{45,12,7}
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    -{45,18,7}-{45,12,7}
TypeError: bad operand type for unary -: 'set'









#SUBSTRACTION:it is a operator which is used to give difference of two operator
#it will not support string , list , tuple , dict
#in set if any common values are present then , it will remove the common value and the result will be always form set 1


{45,18,7}-{45,12,7}
{18}
[45,18,7]-[45,12,7]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    [45,18,7]-[45,12,7]
TypeError: unsupported operand type(s) for -: 'list' and 'list'
(45,18,7)-(45,12,7)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    (45,18,7)-(45,12,7)
TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'

(45:18)-(45:12)
SyntaxError: invalid syntax
{45:18}-{45:12}
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    {45:18}-{45:12}
TypeError: unsupported operand type(s) for -: 'dict' and 'dict'
{45:18}-(45:12)
SyntaxError: invalid syntax
{45:18}-(45,12)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    {45:18}-(45,12)
TypeError: unsupported operand type(s) for -: 'dict' and 'tuple'
  ?mTypeError: unsupported operand type(s) for -: 'dict' and 'dict'
  
SyntaxError: unexpected indent










#MULTIPLICAION:

1*1
1
45.5*8.6
391.3
(2j+4)*(4j+1)
(-4+18j)
True*False
0
'hii'*'byy'
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    'hii'*'byy'
TypeError: can't multiply sequence by non-int of type 'str'
'hii'*2
'hiihii'
[10,20]*3
[10, 20, 10, 20, 10, 20]
(10,20)*3
(10, 20, 10, 20, 10, 20)
{10,20}*3
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    {10,20}*3
TypeError: unsupported operand type(s) for *: 'set' and 'int'
[10,20]*3.5
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    [10,20]*3.5
TypeError: can't multiply sequence by non-int of type 'float'



#IT IS USDE TO PERFORM MULTIPLICATION OF TWO OR MORE OPERANDS #WE CANT DIRECTLY MULTIPLY TWO COLLECTION VALUES FOR THAT  WE SHOULD USE SYNTAX:----->>>>>  operand 1*n, where n is int .


...  
>>> 
>>> 
>>> #      DIVISION OPERATOR:
>>> 
>>> 
>>> # MODULES-->REMAINDER
>>> # DIVISION--> QUOTIENT
>>> 
>>> # it is used to divide given two values
>>> 
>>> #THERE ARE THREE  TYPES OF DIVISION OPERATOR IN PYHTON :
>>> 
>>> #(01)-->> TRUE DIVISION:-->it gives the result as complete quotient when one number is divided with another number
>>> 
>>> 18/4
4.5
>>> #(01)-->> FLOOR DIVISION:-->it gives the result as only integer part from the quotient when a number is divided with another number
>>> 18//4
4
>>> 
>>> #(01)-->> MODULES DIVISION:-->it gives the result as complete remainder when one number is divided with another number
>>> 18%4
2
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #   POWER OPERATOR:
>>> 
>>> 
>>> #   it is used to give the  product for the operands for specified number of times
>>> 
>>> #SYNTAX:--->  operand 1**n
#it is also majorly used on integer and list

1**2
1
5**3
125
6**3
216
7**3
343
8**3
512
9**3
729

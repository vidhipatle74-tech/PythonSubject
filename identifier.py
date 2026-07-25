Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more info
                        #identifire:


 # it is the name of the python program like variable, function, module, object.
 

#rule01:
 
>>> #in identifier part we can use alphabet we can use here uppercase , lowercase & combination of both.
...  
>>> xyz=123
>>> xyz
123
>>> 
>>> XYZ=123
>>> XYZ
123
>>> 
>>> XyZ=123
>>> XyZ
123
>>> 
>>> #Rule02:

>>> #in identifier part should not starts with number but we can use in between or end of the identifier.
>>> 
>>> 45ab="hi"
SyntaxError: invalid decimal literal
>>> 
>>> ab45="hi"
>>> ab45
'hi'
>>> #Rule03:

>>> 
>>> #in identifier parts we cant give special character except (_)underscore
>>> 
>>> a b=624
SyntaxError: invalid syntax
>>> 
>>> ca$sh=764
SyntaxError: invalid syntax
>>> 
>>> ca_sh=599
>>> ca_sh
599

_753=65
_753
65


#rule04:


#in identifier parts we cant use keywords

in=56
SyntaxError: invalid syntax

In=75
In
75

#Rule05:


#in identifier parts we can pass unlimited character but #according to the PEP8 rule we can pass 79 character


#How to check whether the given identifier rule is valid or not ??????
#ANS:  we have to follow the syntax:   "identifier_parts".isidentifier()

# if the rule is valid output should be true
#if the rule is invalid then output should be false


#EXAMPLE:


ca$sh=100
SyntaxError: invalid syntax


"identifier_parts".isidentifier()
True

"ca$sh".isidentifier()
False

123abc=900
SyntaxError: invalid decimal literal

"123abc".isidentifier()
False

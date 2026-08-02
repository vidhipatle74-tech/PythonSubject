Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> r="py
SyntaxError: unterminated string literal (detected at line 1)
>>> r="Python class "
>>> r.count("s",0,12)
2
>>> 
>>> 
>>> 
>>>                         #BOOLEAN METHOD:
>>> 
>>>  #isaplha()
>>> b="kedhdeuydfhehfkr"
>>> b.isalpha()
True
>>> 
>>> 
>>> t="jbeebfewyy786uhj4356GH"
>>> t.isalpha()
False
>>> 
>>> 
>>> 
>>> #isalnum()
>>> 
>>> # combination of alphabet and number
>>> 
>>> #alphabet------> lower
>>>                 #upper
>>>                 #combination               #TRUE
>>> 
>>> 
>>> #only number---->TRUE
>>> #only special character------>FALSE
#alphabet number-->TRUE
#
# alphabet+ nubmer + special character----->FALSE

a="ieddif"
a.isalnum()
True

a="725363"
a.isalnum
<built-in method isalnum of str object at 0x00000202248122B0>
<built-in method isalnum of str object at 0x00000202248122B0>
SyntaxError: invalid syntax





#isdigit()

# syntax---> v_n.isdigit()


#no alphabet--false
# no spl----> false

#only no present in a quotes-->true





#ISUPPER()

#syntax---->  v_n.isupper()

a="LKWWIUQWUIEDGEU78656787^&$^&*&(&"
a.isupper()
True

a="7363763829378*^&%$^&*"
a.isupper()
False


a=("*&^%#@$%^&")
a.isupper()
False

#alphabet(upper)+number+alphabet--->TRUE




#ISLOWER()

#SYNTAX------> v_n.islower()

a="jsgseshffgefjnkgkh7646328(*&^%$#"
a.islower()
True


a="LEJDHUYUlkjdeueifgwud8976754(*&^%$"
a.islower()
False


a="khffhgfrkfj"
a.islower()
True


a=")(*&^%$#"
a.islower()
False


y="skdhheyfeyw9876543)(*&^%$"
y.islower()
True


s="Hi hello"
s.istitle()
False


s="Xyz Abc MNO"
s.istitle()
False




#ISTITLE()
#SYNTAX-----> v_n.istitle()

#ISSPACE()

#SYNTAX---->  V_N.isspace()

s=" "
s.isspace()
True


s="Hi hello"
s.isspace()
False




#STARTSWITCH()

#SYNTAX------>  V_N.startswith('substring', startindex)---->where startindex is optional
#SUBSTRING----> part of the string

y="python class done "
y.startswith("python")
True


y.startswith("class")
False

y.startwith("class",7)
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    y.startwith("class",7)
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
y.startswith("class",7)
True


y.startswith("done",13)
True



#ENDSWITH()

#SYNTAX----> v_n.endswith("substring", si,ei+1)

y="python class done "

e="walmart snapchat instagram dataload"
e.startswith("snapchat")
False

e.startswith("snapchat",8)
True



e.endswith("snapchat")
False


e.endswith("snapchat",8,16)
True


e.startswith("dataload",27)
True


e.endswith("dataload")
True






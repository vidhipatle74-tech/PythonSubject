Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
   #IDENTITY OPERATOR:

# it will check the memory address of the given operands are same or not

#if the address of both the operands are same then it will TRUE
#if the address of both the operands are DIFFERENT then it will FALSE

#TYPES:

#    (1) is operator
#    (2) is  not operator

#(1) is operator:
                 #it will give result as same only if address of pperands are same

#syntax-->>>   operand1 is operand 2

>>> 
>>> 
>>> a=10
>>> b=10
>>> a is b
True
>>> id(a)
140704869565848
>>> id(b)
140704869565848
>>> #the id address of both the operator are same thats why the result has true
>>> 
>>> 
>>> c=10.0
>>> d=10
>>> c is d
False
>>> id(c)
2654777018064
>>> id(d)
140704869565848
>>> #here the id address of both the operands are different thats why the result has false
>>> 
>>> 
>>> #    (2) is  not operator
>>> 
>>> 
>>> #it will give result as same  only if address of 0perands are different
>>> 
>>> #SYNTAX-->  OPERAND1 ID NOT OPERAND2

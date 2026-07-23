Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>>      # ASSIGNMENT OPERATOR:
...      
>>> 
>>> #To assign any value to a variable we required a asssignment operator
...      
>>> #SYNTAX---> var = value
...      
>>> 
>>> a=10
>>> a
10
>>> a=a+10
>>> a
20
>>> a=a+30
>>> a
50
>>> 
>>> # if you want to assign one value to thre variable you can go for assignment operator
>>> 
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> 
>>> 
      #MEMBERSHIP OPERATOR:-


# it will check whether the specified value is present in the collection or not

   #TYPES:

        #There are 2 types of membership operator:


#         (1) in operator
#         (2) not in operator



#         (1) In Operator:


# It will  give the result as true  only the value is present in collection

  

#SYNTAX-->>> value in collection

#we can check
#(1)value in collection
#(2)collection in nested collection

#but not collection in collection and value in individual datatype


#         (2) Not In Operator:

# It will  give the result as true  only the value is  NOT present in  the given collection

#SYNTAX-->>> value  NOT in collection

10 in (45,10,50)
True
12 in (45,10,50)
False
[10,20] in [[10,20],30]
True
[10,20] in [10,20,30]
False
6 in 82637
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    6 in 82637
TypeError: argument of type 'int' is not a container or iterable
'6' in '82637'
True



#NOT IN

34 not in 98765432
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    34 not in 98765432
TypeError: argument of type 'int' is not a container or iterable
34 not in [10,20,30]
True
30 not in [10,20,30]
False

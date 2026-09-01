#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1. Greeting Function
# Write a function that takes a name and prints:
# Hello Amit
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#FUNCTION===>>

#Using print function:-->
"""
def Greet(name):
    print("Hello",name)
Greet("Amit")
"""
#o/p-Hello Amit

#using return keyword:-->
"""
def Greet(name):
    return ("hello",name)
print(Greet("Amit"))
"""
#o/p--> ('hello', 'Amit')

#GENERATOR===>>>

#Using traversing:--->
"""
def Greet(name):
    yield("hello",name)
print(list(Greet("Amit")))
print(tuple(Greet("Amit")))
print(str(Greet("Amit")))
print(dict(Greet("Amit")))
print(set(Greet("Amit")))
"""
#o/p--> [('hello', 'Amit')]
#              (('hello', 'Amit'),)
#              <generator object Greet at 0x0000020E07107400>
#              {'hello': 'Amit'}
#              {('hello', 'Amit')}
    
#Using Looping-->
"""
def greet(name):
    for i in range(1):
        print("Hello", name)
greet("Amit")
"""
#o/p--> Hello Amit
#Using next() function---->
"""
def greet(name):
    for i in range(1):
        yield("Hello", name)
b=(greet("Amit"))
print(b)
print(next(greet("Amit")))
"""
#o/p--> <generator object greet at 0x000001828D570D40>
#              ('Hello', 'Amit')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2. Add Two Numbers
# Write a function that takes two numbers and returns their sum.
# Input: 10, 20
# Output: 30
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCTION====>>>

#Using print function:-->>
"""
def add(a,b):
    print(a+b)
add(10,5)
"""
#o/p---> 15

#Using return keyword-->>
"""
def add(a,b):
    return(a+b)
v=(add(10,5))
print(v)
"""
#o/p--> 15

#GENERATOR===>>>

#Using traversing:
"""
def add(a,b):
    v=a+b
    yield v
b=add(10,5)
print(list(add(10,5))) # [15]
print(set(add(10,5))) #{15}
print(tuple(add(10,5))) #(15,)
print(str(add(10,5))) #generator object address..
"""
#Using  Looping--->
"""
def add(a, b):
    f or i in range(1):
        yield a + b
v=add(10, 20)
for i in v:
    print(i)
"""
#o/p--->> 30

#Using next() function:-->>
"""
def  add(a,b):
    yield(a+b)
v=(add(10,20))
print(next(add(10,5))) #15
"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#(3) Find Difference
# Write a function that accepts two
# numbers and returns their difference.
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#FUNCTION====>>>

#Using print function:-->>
"""
def add(a,b):
    print(a-b)
add(10,5)
"""
#o/p---> 5

#Using return keyword-->>
"""
def add(a,b):
    return(a-b)
v=(add(10,5))
print(v)
"""
#o/p--> 5

#GENERATOR===>>>

#Using traversing:
"""
def add(a,b):
    v=a-b
    yield v
b=add(10,5)
print(list(add(10,5))) # [5]
print(set(add(10,5))) #{5}
print(tuple(add(10,5))) #(5,)
print(str(add(10,5))) #generator object address..
"""
#Using  Looping--->
"""
def add(a, b):
    f or i in range(1):
        yield a - b
v=add(10, 20)
for i in v:
    print(i)
"""
#o/p--->> -10

#Using next() function:-->>
"""
def  add(a,b):
    yield(a-b)
v=(add(10,20))
print(next(add(10,20))) #-10
"""
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#(4)Find Maximum
# Write a function that accepts two numbers and returns the greater number.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#FUNCTION===>>>

#Using print function-->
"""
def Max(a,b):
    if a>b:
        print(f'The given number {a} is greater')
    else:
        print(f'The given number {b} is greater')
Max(10,20)
"""
#o/p--> The given number 20 is greater

#using return keyword--->
"""
def max(a,b):
    if a>b:
        return True
print(max(56,23))
"""
#o/p--> True

#GENERATOR===>>

#Using traversing-->>
"""
def max(a,b):
    if a>b:
        yield True
a=max(56,23)
print(list(max(56,23)))
"""
#o/p--> [True]

##Using looping:-->
"""
def max(a,b):
    for i in range(1):
        if a>b:
            yield True
c=max(56,23)
for i in c:
    print(i)
"""
#o/p--> True

#Using next() function-->
"""
def max(a,b):
    if a>b:
        yield True
print(next(max(56,23)))
    """
#o/p--> True
#             True
  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 5. Find Minimum
# Write a function that accepts two
# numbers and returns the smaller number.
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------

#FUNCTION===>>>

#Using print function-->
"""
def Min(a,b):
    if a<b:
        print(f'The given number {a} is smaller')
    else:
        print(f'The given number {b} is smaller')
Min(10,20)
"""
#o/p--> The given number 20 is greater

#using return keyword--->
"""
def min(a,b):
    if a<b:
        return True
print(min(56,23))
"""
#o/p--> True

#GENERATOR===>>

#Using traversing-->>
"""
def min(a,b):
    if a<b:
        yield True
a=min(56,23)
print(list(min(56,23)))
"""
#o/p--> [True]

##Using looping:-->
"""
def min(a,b):
    for i in range(1):
        if a<b:
            yield True
c=min(56,23)
for i in c:
    print(i)
"""
#o/p--> True

#Using next() function-->
"""
def min(a,b):
    if a<b:
        yield True
print(next(min(56,23)))
    """
#o/p--> True

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 6. Check Even or Odd
# Write a function that accepts a number
# and returns "Even" or "Odd".
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#FUNCTION==>>

#Using print() function--=>
"""
def even_odd(a,b):
    if a%2==2:
        print(f"the number {a} is even number")
    else:
        print(f"the number {b} is odd number")
even_odd(20,21)
"""
#o/p--> the number 20 is even number

#Using return keyword--->
"""
def even_odd(a,b):
    if a%2==0:
        return True
print(even_odd(56,34))
"""
#o/p--> True

#GENERATOR====>>>



    


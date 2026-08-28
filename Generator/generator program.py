"""
#function-->
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    return a
    return b
    return c
d=check(10,20)
print(d)
"""
#generator-->
"""
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c
q=check(10,20)
print(q)

#o/p--><generator object check at 0x0000027662433220>

#To convert it into readable format we use--> typecasting , looping and next():
print(list(q))

#o/p--> [30, -10, 200]


print(next(q))"""
#after performing all operation on yield if we are calling more than three it will show stop iteration error :
#like --->
"""
   print(next(q))
StopIteration
"""
"""
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c
m=check(10,20)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
"""

#with extra -->
"""
def check(x,y):
    a=x+y
    b=x-y
    c=x*y
    yield a
    yield b
    yield c
m=check(10,20)
print(check(m))
"""
#after performing the 1st operation if i want to stop the flow of the execution then we use [m.close]
#after  if i will calling next print function-----> it will through stopiteration error..


#que-->

v=[1,2,3,4,5,6]
"""
def square(v):
    for i in v:
        print(i**2)
square([1,2,3,4,5,6])
"""
#o/p--> 1
#           4
#           9
#          16
#          25
#          36
"""
def square(v):
    for i in v:
        yield(i**2)
z=square([1,2,3,4,5,6])
print(z)

#o/p--> <generator object square at 0x000001CFF26BCD40>

print(next(z))
print(next(z))
z.close
"""
#o/p--> show output only 1,2      after i call next print function it will through stopiteration error

"""def square(v):
    l=[]
    for i in v:
        yield(i**2)
    return l
z=square([1,2,3,4,5,6])
print(z)
"""

a=["walmart","vistara","vistar","blind","thankyou","promax","panker"]
"""
def odd(a):
    l=[]
    for i in a:
        if  len(i)%2==1:
            l.append(i)
    print(l)
odd(["walmart","vistara","vistar","blind","thankyou","promax","panker"])
"""

 #yield-->

def odd(a,b):
    l=[]
    
    for i in a:
        if  len(i)%2==1:
            l.append(i)
    yield(l)
    yield(l)
p=odd(["walmart","vistara","vistar","blind","thankyou","promax","panker"])
print(next(p))
print(next(p))

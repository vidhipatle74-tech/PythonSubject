#Default parameter:


# syntax:
"""
             def function_namr (v_n=0,v_n=0,v_n=0):
                 statement
            function_name(arguments)

"""

#1--> positional parameter-->
"""
def spam(x,y,z):
     print(x,y,z)
spam(1,2,3)
"""
#o/p--> 1 2 3

#2--> keyword parameter-->
"""
def spam(x,y,z):
     print(x,y,z)
spam(x=1,y=2,z=3)
"""
#o/p--> 1 2 3


#3--> only positional argument-->
"""
def spam(a,b,/,c,d,e):
    print(a,b,c,d,e)
spam(20,30,c=40,d=50,e=60)
"""
#o/p--> 20 30 40 50 60

#4--> only keyword argument-->
"""
def spam(a,b,*,c,d,e):
    print(a,b,c,d,e)
spam(10,20,c=30,d=78,e=50)
"""
#o/p--> 10 20 30 78 50

#5--> combination of / and * symbol argument-->
"""
def spam(a,b,/,c,*,d,e):
    print(a,b,c,d,e)
spam(10,20,30,d=78,e=50)
"""
#o/p--> 10 20 30 78 50

#6--> variable positional argument-->
"""
def spam(*args):
    print(args)
spam()
#o/p--> ()
spam(1)
#o/p--> (1,)
"""
"""
def spam(*args):
    print(*args)
spam(1,2,"vidhi",687)

#o/p--> 1 2 vidhi 687
"""


#6--> variable keyword argument-->

def spam(**kwargs):
    print(kwargs)
spam(b=10,c=40)

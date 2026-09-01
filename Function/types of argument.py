 R#while calling the argument , there are some types of arguments:

#(1)-->* positional argument*                      ---->imp
#(2)-->* keyword  argument*                      ----> imp
#(3)--> only positional argument
#(4)--> only keyword argument
#(5)--> *variable positional argument -->(*args )*           ---->imp
#(6)--> *variable keyword argument --> (**kwargs)*       ----> imp
#(7)--> combintion of only positional argument and only keyword argument
#(8)--> combination of *args and **kwargs



#positional argument-->

""" how many parameters you are  passing , that much argument you need to pass """
"""any one argument mismatch it will show error """
#if i not pass anything in positional argument  then it will show error.(TYPE ERROR)

"""
  def demo (a,b,c):
      print(a,b,c)
 demo(1,2,3)
 """
#here,
#         parameter==argument

#if

# demo(1,2)---->  1-error
#demo (1)-----> 2-error
#demo( )-----> 3-error

#(2)-->* keyword  argument* :

"""firstly we need to declare  parameter after that we need to pass value with parameter """
""" if i pass direct value to parameter it wil act like a positional argument"""

 #syntax:
"""           parameter =argument    """

'''
def demo (x,y,z):
    print(x,y,z)
demo(x=10,y=20,z=30)
'''

#here:

#demo(10,20,z=30)
#demo(x=10,y=20)----> error
#demo(x=10)-----> error
#demo()--> error


# demo(1,2)---->  1-error 

#(3)--> only positional argument(/):

#    --> before the / symbol we can pass only positional argument
#          but,
#          after / symbol  we can pass  both positional and keyword argument


#   question   --> what is the difference between forward slash and astric symbol.
#                   --> before the


"""
def spam(a,b,/,c,d,e):
    print(a,b,c,e,d)
spam(20,30,c=40,d=50,e=60)
#o/p--> 20 30 40 60 50
spam(a=10,b=20,c=30,)
"""


#(4)--> only keyword argument:-->

#---> before the * symbol we can pass both positional and keyword argument
#       but,
#       after * symbol we can pass only keyword argument
"""
def spam(a,b,*,c,d,e):
    print(a,b,c,e,d)
spam(20,30,c=40,d=50,e=60)
#o/p--> 20 30 40 60 50
"""

#(5)--> combination of positional and keyword arguments:


#(6)-->  variable positional argument(*args):
#                             ---> it is a property
#                              ---> (* agrs)----> return type will be tuple
#                             ---> here we can pass unlimited data
#                             ---> * is mandatory
#                             ---> in the place of agrs and we can pass any
#                             ---> here if i not pass any thing it will won't show any eror it will return empty tuple.


#in program--> print(args)---> if we print only args , output should be in packed format

#                       print(*args)---> if we print *args , output should be in unpacked format.
"""
def spam(*args):
    print(args)
spam()
#o/p--> ()
spam(1)
#o/p--> (1,)
spam(1,2,3,"hii",4,5)
#o/p--> (1, 2, 3, 'hii', 4, 5)
"""

#(7)-->  variable keyword argument(**kwargs):

#                                  ---> it is a property
#                                  ---> here we can pass unlimited data
#                                  ---> return type of (**kwargs)---> dictionary format
#                                 --->

#in program--> print(kwargs)---> if we print only kwargs , output should be in packed format

#                       print(*kwargs)---> if we print *kwargs , output should be in unpacked   format only in keys.

#                      print(**kwargs)---> we cant use that it will show error--> because ---

"""
def spam(**kwargs):
    print(kwargs)
spam()
#o/p--> {}
spam(a=10)
#o/p--> {'a': 10}
spam(x=10,y=39,z=[1,2])
#o/p--> {'x': 10, 'y': 39, 'z': [1, 2]}
spam()
"""

"""
def spam(**kwargs):
    print(**kwargs)
spam()
#o/p--> blank space
"""
"""
def spam(**kwargs):
    print(*kwargs)
spam(a=10,b=20,c=30)
#o/p--> a b c ---> output in unpacked format and only keys .
"""

"""
def data(*args,**kwargs):
    print(args,kwargs)
data()
#o/p--> () {}
data(10,20,a=20,b=30)
#o/p--> (10, 20) {'a': 20, 'b': 30}
"""

def data(*args,**kwargs):
    print(*args,*kwargs)
data()
#o/p--> blabk space
#all output in unpacked format






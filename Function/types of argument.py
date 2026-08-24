#while calling the argument , there are some types of arguments:

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

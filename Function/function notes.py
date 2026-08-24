#function:
#            --> It is defined  as the set of code / block of code it will execute  when we calling the function.
#           --> Without calling function if we execute ,  it will show blank space.

#Types of function:
#                            (1)--> predefined function / inbuilt function
#                                  -->[round(),abs(),isinstance(),]
#                              --> its already defined , no need to change, no need to modify,nothing.

#                            (2)--> User-defined function

                                  #User-defined syntax:
#                                                                  |
#                            -------------------------------------------------------
#                           |                                                                                  |
#      (1) without using return keywords                          (2)with using return keywords

#(1) Without using return keywords :


#SYNTAX:
"""
                def function_name (parameter):       #--->( function declaration)
                 |
                 |           statement                               #-->( block of code / set of code)
                 |           statement
                 |
                 function_name (argument)                #--> ( function calling )
"""
#Where,
#           def--> keyword
#           function_name--> name of the program (any program)
#           parameter--> its optional ( it means variable name )
#           arguments--> its optional ( it means variable value )


#--> parameter always pointing to argument.



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




#program :

"""
def even(a):
     if a%2==0:
         print(f'The given number {a} is even')
     else:
         print(f'The given number {a} is odd')
even(10)
"""
#o/p--> The given number 10 is even

"""
def even_odd():
    num=int(input("enter the number:"))
    if num%2==0:
         print(f'The given number {num} is even')
    else:
        print(f'The given number {num} is odd')
even_odd()
"""
#o/p-->   enter the number:77
#             The given number 77 is odd

#wap to check whether the word is palindrome or not.
"""
def palindrome(s):
    if s==s[::-1]:
        print("its palindrome")
    else:
        print("its not palindrome")
palindrome("level")
palindrome("python")
palindrome("mom")
"""
#o/p-->
#           its palindrome
#           its not palindrome
#           its palindrome


#even number.
"""
d=["hii","walmart","xyz","good","onoff"]

def even_length(d):
    for i in d:
        if len (i)%2==0:
            print(i)                                                                       #remaining..
        else:
            print(i[::-1])
even_length("hii","walmart","xyz","good","onoff")
"""


#
"""
s="hello"

def data(s):
    k={}
    for i in s:
        k[i]=ord(i)
    print(k)
data("hello")
data("vidhi")
"""
#o/p--> {'h': 104, 'e': 101, 'l': 108, 'o': 111}
#            {'v': 118, 'i': 105, 'd': 100, 'h': 104}

#
"""
d=[1,45,78,True,False,999]

def data(d):
     for i in d:
         if isinstance(i,bool):
             print(i)
     print()
data(1,45,78,True,False,999)
 """   
###########
"""
e=[90,True,3.5,9+4j,"abc",[1,2,3],{67,90}]

a=[]
b=[]
for i in e:
    if isinstance(i,(complex,bool,int,float,)):
        a.append(i)
    else:
        b.append(i)
print(a)
print(b)
"""
#o/p-->    [90, True, 3.5, (9+4j)]
#               ['abc', [1, 2, 3], {90, 67}]


e=[90,True,3.5,9+4j,"abc",[1,2,3],{67,90}]

def data(e):
    a=[]
    b=[]
    for i in e:
         if isinstance(i,(complex,bool,int,float,)):
              a.append(i)
         else:
             b.append(i)
    print(a)
    print(b)
data(90,True,3.5,9+4j,"abc",[1,2,3],{67,90})
    
    

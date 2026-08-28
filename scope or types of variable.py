#SCOPE:-->
#   -->  the place of variable

#TYPES OF VARIABLE :
#                                  (1)--> local variable
#                                  (2)--> global variable
#                                  (1)-->  non-local variable

#LOCAL VARIABLE:
#                            --> any variable present inside the function then we call it as a local variable.

#                            --> local variable we cant access directly if we access  it will show name error.

#                          -->how to access local variable outside??---> (by the help of return keyword)

#Example(1):
"""
                def spam( ):
                    name='python'               -----> local variable 
                    print(python)
                spam()
"""
#inside it will give output.
#outside it will show name error.


#Example(2):
"""
         def spam():
             name='python'
             return name
        q=spam()
        print(q)            ----------> python
"""

#GLOBAL VARIABLE :
#                              --> any variable is present outside  the  function then we can call it as a global variable 
#                              --> global variable we can access any where  into the function  means inside the function
#                                    or outside the function it will work
#                              --> in global variable we can do modification outside without using any keyword
#                             ---> but if we done any modification  inside the function without keyword it will show unboundedlocal error.

#How to do modification for global variable inside ----->

#                --> using global keyword we can do modification inside .

#Example:-->
"""
a=100     #global variable
def display():
    global a
    b=10      #local variable
    print(f'the given variable is local variable {b}')
    a=a+400
    print(f'the given variable is global variable {a}')    #500

diaplay()
print(f'the given variable is global variable {a}')   #500
print(f'modification for global variable (outside)')
a=a+400
print(a)   #900
"""


#NON-LOCAL VARIABLE-->
#                                      --> any variable is present in between two function that type of variable  we can call it as a non local variable
#                                      --> neither global nor local in between two function what variable  we are passing that one we can call it as a
#                                            non local variable.
#                                       --> how to do modification in non local variable m(outside)?????----> using non local keyword...

#Example:-->
"""
        x=10                          #-->global variable 
        def outer ():
            y=20                     #---> non local variable 
            print(x) #      works
            print(y)#       works

            def inner():
                z=30                 #-->local variable
                print(x)
                print(y)
                print(z)
            inner()
            print(x)#----> works 
            print(y)# ---> works 
            print(z) # ----> wont work
       outer()
       print(x)# ---> works
       print(y)# ---> name error
       print(z)# ----> name error
"""

#Example:-->
x=10
def outer():
    y=20
    print(x)
    

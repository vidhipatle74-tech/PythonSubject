#instance method-->

#Instance is an object
# Instance method only working on object data
#In instance method object creation is mandatory

# A method which will accepts  first parameter of an object address then we can call it as a instance method

#SYNTAX:-->

"""
     def classname:
         def method_name (self)
                 statement
                 statement
    object=classname()
"""
#here,
#          self is always pointing to object.

#How can we access instance method outside.
"""
#(1)--> by using object:

#          synatx:
#                          object.method_name     or       object.method_name(object)
#                    (.....explicitly we have to use object....)

#(2)--> by using classname:

#syntax:
#                 classname.method_name(object)

"""

#How can we access class variable  into instance method
"""
#(1)--> by using classname :

#syntax:
#               classname.class_variable_name

#(2)--> by using object:

#syntax:
#                object_name/self.class_variable_name
"""

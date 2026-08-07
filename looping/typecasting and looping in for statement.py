#for loop-->
#syntax(1):
#          for variable in iterable:
#          <--> statement.


#syntax(2):
#          for i in range(startpoint, endpoint,stepvalue)
#          <--> statement.

#ENUMERATE-->To print both char and numbers.

#SYNTAX-->     enumerate(iterable)


s="hello"
'''
normal synatx--->enumerate(iterable)
              |
data will convert to object address
              |
two ways--1>typecasting            2-->looping
              |                          |
syntax for typecasting             syntax for looping:                 
list(enumerate(iterable))                |
tuple(enumerate(iterable))      for variable in enumerate(iterable):
dict(enumerate(iterable))          statement
set(enumerate(iterable))



# output of enumerate function:--->(position,value)
'''
#way 1 is:-->typecasting.
'''
print(list(enumerate(s)))

             #outpit-->[(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]

print(set(enumerate(s)))

             #output--> {(4, 'o'), (0, 'h'), (2, 'l'), (3, 'l'), (1, 'e')}

print(dict(enumerate(s)))

             #output-->{0: 'h', 1: 'e', 2: 'l', 3: 'l', 4: 'o'}

print(tuple(enumerate(s)))

             #output--> ((0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')

#way 2 is ---> looping:

for i in enumerate(s):  #-->  #to pront both position and character. (in packed formate)
    print(i)

    #output-->
              (0, 'h')
              (1, 'e')
              (2, 'l')
              (3, 'l')
              (4, 'o')


s="hello"
for i,j in enumerate(s): #----> #To print only position of the given example (in unpacked formate)
    print(i)

    #output-->
              0
              1
              2
              3
              4

'''
k=[10,20,30,40,50]
for i in enumerate(k):
    print(i)

     #output--> (0, 10)
                (1, 20)
                (2, 30)
                (3, 40)
                (4, 50)


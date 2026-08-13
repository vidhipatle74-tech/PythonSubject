#WHILE LOOP:

#         -->  a set of instruction/block of code which will execute
#              repeteadly until the condition is satisfied

#SYNTAX:-->
#          initialization
#          while condition:
#          <---> statement block/logic
#                updation


#if updation is skipped then loop will be converted to infinite loop.

#wap to print "idli vada " 5 times.
"""
i=0
while i<5:
    print("idli vada")
    i+=1

#o/p--> idli vada
        idli vada
        idli vada
        idli vada
"""
#wap to print the 1-10 in reverse
"""
i=10
while i>=1:
    print(i,end=" ")
    i-=1

#o/p--> 10 9 8 7 6 5 4 3 2 1
"""
#wap to print the number from 1-10.
'''
i=0
while i<11:
    print(i,end=" ")
    i+=1
'''
#wap to print the even number from 1-50 in reverse order.
"""
i=50
while i>=1:
    if i%2==0:
        print(i,end=" ")
    i-=1

#o/p--> 50 48 46 44 42 40 38 36 34 32 30 28 26 24 22 20 18 16 14 12 10 8 6 4 2 
"""

#wap to print  sum of  natural number
"""
n=int(input("enter the number"))
i=1
sum=0
add=0
while i<=n:
    add=add+i
    i+=1
print(add)

#o/p---> enter the number10
         55
"""
#wap a print multiplication of natural number
"""
n=int(input("enter the number"))
i=1
mul=1
while i<=n:
    mul=mul*i
    i+=1
print(mul)

#o/p-> enter the number10
       3628800

"""
#wap to fetch the lowercase character from a string.
"""
a=input("enter the string")
out=" "
i=0

while i<len(a):
    if a[i].islower():
        out=out+a[i]
    i+=1
print(out)

#o/p-->    enter the string"ViDhI"
           ih
"""

#wap to fetch the lower,upper,digit,special character.
'''
v=input("enter the string")
lower=''
upper=''
digit=''
specialchar=''
i=0

while i<len(v):
    if v[i].islower():
        lower=lower+v[i]
         
    elif v[i].isupper():
            upper=upper+v[i]
            
    elif v[i].isdigit():
        digit=digit+v[i]
        
    else:
        specialchar=specialchar+v[i]              
    i+=1
print(lower)
print(upper)
print(digit)
print(specialchar)

#o/p--> enter the string'vidhiADR123#$%'
        vidhi
        ADR
        123
       '#$%'
'''

'''
#wap to print addition of integer number.
b=[10,4j+9,'SHR','DON',45,90,'di']
i=0
sum=0
a=''
                                       #remaining
while i<len(b):
    a=a+i
    i+=1
print(a)
'''


#wap to print srt value from a list  only if len is >3

st=eval(input(" enter the list:"))
i=0
while i<len(st):
    if type(st[i])==str and len(st[i])>3:
        print(st[i])
    i=i+1

#wap to do addition of ascii value of the special character in the given string.
"""
s=(input("enter the string:-"))
i=0
total=0

while i< len(s):
    if not s[i].isalnum() and s[i] !=" ":
        total=total+ord(s[i])
    i=i+1

print(" sun of ASCII value of special character:",total)
"""

#o/p-->enter the string:-H@He!!
#      sum of ASCII value of special character: 130

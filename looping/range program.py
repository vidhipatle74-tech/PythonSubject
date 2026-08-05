#range()----> startpoint---->endpoint---->stepvalue..


#wap to print the number vberticaly
'''
for i in range(10):
    print(i)
'''
#wap to print number horizontaly
'''
for i in range(10):
    print(i,end=" ")
print()
'''
#wap to print the number between 15-20
'''
for i in range(15,30):
    print(i)
'''
#wap a program to print 10-20 in between even numbers
'''
for i in range(10,21):
    print(i)
'''


'''
for i in range(10,21,1): 
    if i%2==0:                         ------>even number
        print(i,end=" ")
print()
'''

'''

for i in range(10,20,2):
    print(i,end=" ")
''' 

#wap to print 10 to 1 in reverse
'''
for i in range(10,1,-1):
    print(i)
'''

#wap to print 50 to 35 in reverse
'''
for i in range(50,35,-1):
    print(i)

'''

#wap to print position of the character in the given string.

s="python"
#o/p-->0,1,2,3,4,5
''' 
for i in range(0,6):                   #for in in range(len(s)):
    print(i)

'''
'''
for i in range(len(s)):                
    print(i,s[i])

'''


s=["morning","walmart","hello","joy","part"]
'''
for i in range(len(s)):
    print(i)
'''
'''

for i in range(len(s)):
    print(i,s[i])

'''

#wap to print sum of the number

'''
Total=0
for i in range(0,11,1):     ---->only 1 to 10 number will be printed
    print(i)
'''

'''
Total=0
for i in range(0,11,1):     #-----> sum of 0 to 10 number (final output--55) 
    Total=Total+i
print(Total)
'''

#wap to print list with key and values
'''
s="Hello"
x={}

for i in s:                #var_name[key]=value    #this syntax --to store the character outside
    #x[i]=ord(i)
    x.update({i:ord(i)})   #var_name.update({kay:value})
print(x)
'''

#wap to count uppercase character
'''
s="PyTHon"
total_character=0
for i in s:
    if i.isupper():
        total_character=total_character+1
print(total_character)
'''

#wap to count uppercase character
'''
s="PyTHon"
total_character=0
for i in s:
    if i.islower():
        total_character=total_character+1
print(total_character)
'''

#square from 1 t0 10
'''
for i in range(1,11):
    print(i**2)
    
'''

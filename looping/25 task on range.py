#Practice Questions

#(1)Print each character of a string
'''
a="Tree Notes"

for i in a:
    print(i,end='')
'''

#-----------------------------------------------------------------------------------------------------------------------------
#(2)Print vowels only

'''
s = "education"

for i in s:
    if i in "aeiouAEIOU":
        print(i)
'''
#-------------------------------------------------------------------------------------------------------------------------------
#(3)Count uppercase letters

'''
s = "PyTHon"
char=0
for i in s:
    if i.isupper():
        char=char+1
print(char)
 '''   
   
#------------------------------------------------------------------------------------------------------------------------------
#(4)Print digits from string
'''
s = "ab12cd34"

for i in s:
    if i.isdigit():
        print(i)
'''
#-----------------------------------------------------------------------------------------------------------------------------
#(5)Sum of list elements

'''
x=[25,70,90,100]
y=0

for i in x:
    y=y+i
print(y)
'''   
#----------------------------------------------------------------------------------------------------------------------------
#(6)Print even numbers from list
'''
e=[23,45,66,78,90]


for i in e:
    if i%2==0:
        print(i)
'''    
#------------------------------------------------------------------------------------------------------------------------------
#(7)Print negative numbers
'''
l = [4,-2,7,-9,3]

for i in l:
    if i<=0:
        print(i)
'''
#-----------------------------------------------------------------------------------------------------------------------------
#(8)Count odd numbers
'''
l = [1,2,3,4,5,6,7]

for i in l:
    if i%2==1:
        print(i)
'''
#-------------------------------------------------------------------------------------------------------------------------------
#(9)Print odd numbers 1 to 20
'''
for i in range(1,20):
    if i%2==1:
        print(i)
'''
#-----------------------------------------------------------------------------------------------------------------------------
#(10)wap Sum from 1 to 50
'''
Total=0
for i in range(1,50):
    Total=Total+i
print(Total)
'''
#----------------------------------------------------------------------------------------------------------------------------    
#(11)wap Print numbers divisible by 5 (1 to 51)
'''
for i in range(1,51,1):
    if i%5==0:
        print(i)
'''
#----------------------------------------------------------------------------------------------------------------------------
#(12)Reverse 10 to 1
'''
for i in range(10,1,-1):
    print(i)
'''
#--------------------------------------------------------------------------------------------------------------------------
#(13)Squares from 1 to 10
'''
for i in range(1,10,1):
    if i%2==0:
        print(i)
'''
#----------------------------------------------------------------------------------------------------------------------------
#(14)Print ASCII values of characters

'''
s='ABC'

for i in s:
    print(ord(i))
'''
#-----------------------------------------------------------------------------------------------------------------------------
#(15)wap to Count consonants
'''
total=0
s = "education"
for i in s:
    if i not in "aeiouAEIOU":
        print(i)
'''
#------------------------------------------------------------------------------------------------------------------------------
#(16)Print numbers greater than 50
'''
l = [23,67,12,89,54]

for i in l:
    if i>50:
        print(i)
'''
#-----------------------------------------------------------------------------------------------------------------------------
#(17)Count positive numbers
'''
l = [-1,4,-3,7,9]

for i in l:
    if i>0:
        print(i)
'''
#-----------------------------------------------------------------------------------------------------------------------------
#(18)wap to Separate even/odd
'''
e=[1,2,3,4,5,6,7,8]

x=[]
y=[]
for i in e:
    if i%2==0:
        x.append(i)
                             
    else:
        y.append(i)
print(x)  
print(y)
'''
#------------------------------------------------------------------------------------------------------------------------------
#19.Sum of even numbers
'''
e=[1,2,3,4,5,6,7,8]
f=0

for i in e:
    if i%2==0:
        f=f+i
print(f)
'''
#----------------------------------------------------------------------------------------------------------------------------
#(20)wap to print the number form 1 -20 segregate even and odd number into list.
'''
w=[]
x=[]
for i in range(1,20,1):
    if i%2==1:
        w.append(i)
    else:
        x.append(i)
print(w,end=" ")
print(x,end=" ")
'''
#--------------------------------------------------------------------------------------------------------------------------
#(21)wap to extract vowels and digits in a string
'''
s="hello123"

for i in s:
    if i in "aeiouAEIOU":
        print(i)

    else:
        s.isdigit()
print(i)

'''
#----------------------------------------------------------------------------------------------------------------------------
#(22)wap to capitalize only the first letter of every word in the given list
'''
l=["vaidegi","rahul","shivam","kapil","patil"]

for i in l:
    print(i.capitalize())
'''
#---------------------------------------------------------------------------------------------------------------------------
#(23)wap to extract only individual data types form the list
'''
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]

for i in l:
    if isinstance(i,(int,float,bool,complex)):
        print(i)
       
'''
#---------------------------------------------------------------------------------------------------------------------------
#(24)wap to extract only individual data types from the list and sum all the individual data types
'''
l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
m=0
for i in l:
    if isinstance(i,(int,float,bool,complex)):
        m=m+i
        print(m)
'''      
#----------------------------------------------------------------------------------------------------------------------------
#(25)wap to print the count of alphabets and numbers and space in the given string
'''
s="india got the independence in the year 1947"

alphabet=0
number=0
space=0

for i in s:
    if i.isalpha():
        alphabet=alphabet+1

    elif i.isdigit():
            number=number+1
    elif i.isspace():
        space=space+1
print('The count of alphabet is:',alphabet)
print('The count of digit is:',number)
print('The count of space is:',space)
            
'''
----------------------------------------------------------------------------------------------------------------------------
#26.wap to check how many words are present
# in the given sentence
a="hello world sentence"
b=a.split()
print(b) #['hello', 'world', 'sentence']
total=0
for i in b:
    total=total+1
print(total)
'''
--------------------------------------------------------------------------------------------------------------------------
# 27.wap to create a dictionary and print the characters
# and its Ascii value pair
s="hello world"
# output:--> {"h":ascii value,"e":ascii value........}
d={}
for i in s:
    d.update({i:ord(i)})
print(d)

d={}
for i in s:
    d[i]=ord(i)
print(d)
'''
---------------------------------------------------------------------------------------------------------------------------------------
'''
# 28.wap to create a dictionary and
# traverse into it and if the length is
# even print as it else reverse it
names=["apple","google","yahoo","microsoft","gmail","walmart"]
# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}
d={}
for i in names:
    if len(i)%2==0:
        d[i]=i
    else:
        d[i]=i[::-1]
print(d)
'''
----------------------------------------------------------------------------------------------------------------------------------------
# 29.wap to print series of factorial(take user input)
num=eval(input("enter the Number"))
fact=1
for i in range(1,num+1,1):
    fact=fact*i
    print(i)
print(fact)
"""
fact=1
i=1
fact=fact*i----> fact=1*1----=1
i=2
fact=fact*i----> fact=1*2----=2

i=3
fact=fact*i----->fact=2*3----=6

i=4
fact=fact*i---> fact=6*4----=24

i=5
fact=fact*i---> fact=24*5---=120    
 ----------------------------------------------------------------------------------------------------------------------------------------------
#(30)wap to create a dictionary with element and its count pair.
l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
'''
a={}
for i in l:
    a [i]=l.count(i)
print(a)

#output-->{'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}
'''
--------------------------------------------------------------------------------------------------------------------------------------------------
      

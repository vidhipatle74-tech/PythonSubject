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
    
    








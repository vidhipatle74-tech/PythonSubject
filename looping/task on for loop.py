#1.WAP to return a dictionary with word & its
'''
#from a string
string = 'hello good morning how are youu'
#exp o/p : {hello:5, guys:4, morning:7, how:3,are:3, you:4}

s= 'hello good morning how are youu'
d={}
for i in s.split():
    d.update({i:len(i)})#with using inbuilt
    #    OR
    # d[i]=len(i)  #without useing inbuilt
print(d)
'''
'''
#2.WAP to count number of vowels present in given
string

s = 'GooD mOrnIng'
vowel_count=0
for i in s:
    if i in "AEIOUaeiou":
        vowel_count=vowel_count+1
print("total vowels in the Given string--->",vowel_count)
'''
'''
#3.WAP to get below o/p:
s = 'Hi how are you'
#exp o/p : 'iH woh era uoy'

s = 'Hi how are you'
res=" "
for i in s.split():
    res=res+" "+i[::-1]
print(res)
'''
'''
#4.WAP to print all the digits in a below list
l = ['hello', '123', 'hai', 'python', '345']
for i in l:
    if i.isdigit():
        print(i)

'''
'''
#5.WAP to check whether string is ANAGRAM or not
#anagrams : characters should be same it can 
different meaning
#tea, eat
#silent, listen
#bored , robed
#cat, act
#keep, peek
#lamp, palm

a="tea"
b="eat"
print(sorted(a,reverse=False))
print(sorted(b))
#['a', 'e', 't']==['a', 'e', 't']
if sorted(a)==sorted(b):
    print("its a Anagram")
else:
    print("its not")
'''
'''
#6.Find the sum of even numbers from 1 to 20
a=0
for i in range(1,21,1):
     if i%2==0:
         a=a+i
         print(a)
 '''        
'''
#7.Count numbers divisible by 3 from 1 to 50

for i in range(1,50,1):
    if i%3==0:
        print(i)


'''
'''
#8.Replace negative numbers with 0

num= [10, -5, 20, -3, 40]
for i in range(len(num)):     #0 1 2 3 4
    if num[i]<0:              #10<0--->False -5<0
        num[i]=0
print(num)

'''
'''
#9.Print position of each character
word = "PYTHON"

for i in word.split():
    if i

1 P
2 Y
3 T
4 H
5 O
6 N
'''

#10.Count even and odd numbers in a list.
num= [10, 15, 22, 31, 40, 51]
a={}
b={}

for i in num:
    if num%2==0:
        print(a)
    else:
        print(b)
            






'''
#11.wap to print repeated char and count the same
s="helloworld"


#12.Grouping flowers and animals separately
items=["lotus-flower","lilly-flower","cat-animal","dog-animal","sunflower-flower"]


#13.filter only character except digits
s="Think456 and 123answers it789 guys "

#14.replace whitespaces with newline char 
# in the below string
s="hello world welcome to python"

#15.replace all vowels with *
s="hello world welcome to python"


#wap to check the given number is Armstrong number
#or Not.
a=153
total=0
b=str(a) #------->153------>'153'
print(b)  #-------->iterable
power=len(b)
print(power)  #----->'153'------->3
for i in b:  #i--->'1' i---->'5' i----->'3'
    total=total+int(i)**power  #power---->3
    #0   =0    + 1**3
if total==a:
    print("its a Armstong number")
else:
    print('its Not')

#wap to print 2 to 10 table
for i in range(1,11):
    for j in range(2,11):
        print(i*j,end=" ")
    print()
#----------------OR
for i in range(1,11):
    for j in range(1,11):
        print(f'{i} * {j}----->{i*j}')
    print()
    


a="Good day"
for i in range(len(a)):
    print(i+3,a[i])
print()

            OR
for i in enumerate(a,start=3):
    print(i)

for variable in enumerate(iterable,start=number):
    statement
'''

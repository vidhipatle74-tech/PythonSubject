#1. Greeting Function
#Write a function that takes a name and prints:
#Hello Amit
"""
def greet(name):
    print("hello",name)
greet("amit")
"""
#o/p--> hello amit

#2. Add Two Numbers
#Write a function that takes two numbers and returns their sum.
#Input: 10, 20
#Output: 30
"""
def add(a,b):
    return(a+b)
print(add(10,20))
"""
#o/p--> 30

#3. Find Difference
#Write a function that accepts two numbers and returns their difference
"""
def function(a,b):
    return a-b
print(function(45,77))
"""
#o/p--> -32

#4. Find Maximum
#Write a function that accepts two numbers and returns the greater number.


#without using inbuilt function:
"""
def maximum(a,b):
    if a>b:
        print(f'the number {a} is a greater  number')
    else:
        print(f'the number {b} is greater number')
maximum(45,54)
"""
#o/p--> the number 54 is greater number

#with using inbuilt function:
"""
def maximum():
    num1=eval(input("enetr the number:"))
    num2=eval(input("enter the number:"))
    print(max(num1,num2))
maximum()
"""
#o/p--> enetr the number:21
#           enter the number:23
#           23

#5. Find Minimum
#Write a function that accepts two numbers and returns the smaller number.
"""
def minimum(a,b):
    if a<b:
        print(f'The number--> {a} is smaller number')
    else:
        print(f'the number--> {b} is smaller number')
minimum(21,23)
"""
#o/p--> The number--> 21 is smaller number

#6. Check Even or Odd
#Write a function that accepts a number and returns "Even" or "Odd".
"""
def even_odd(a):
    if a%2==0:
        print(f'The number--> {a} is even')
    else:
        print(f'The number--> {a} is odd')
even_odd(21)
"""
#o/p--> The number--> 21 is odd

#7. Check Positive, Negative or Zero
#Write a function that accepts a number and returns:
#Positive
#Negative
#Zero
"""
def p_n_z(x):
    if x>0:
        print(f'The number--> {x} is positive')
    elif x<0:
        print(f'The number--> {x} is negative')
    else:
        print(f'The number--> {x} is zero')
p_n_z(45)
p_n_z(-45)
p_n_z(0)
"""
#o/p--> The number--> 45 is positive
#            The number--> -45 is negative
#            The number--> 0 is zero

#8. Square a Number
#Write a function that accepts a number and returns its square.
#Input: 5
#Output: 25
"""
def square(a):
    return a**2
print(square(5))
"""
#o/p--> 25

#9. Cube a Number
#Write a function that accepts a number and returns its cube.
"""
def cube(a):
    return a**3
print(cube(3))
"""
#o/;--> 27

#10. Find Last Digit
#Write a function that accepts a number and returns its last digit.
#Input: 12345
#Output: 5
"""
def last_digit(a):
    return a%10
print(last_digit(12345))
"""
#o/p--> 5

#(11). Find First Digit
#Write a function that accepts an integer and returns its first digit.
#Input: 45678
#Output: 4
"""
def first_digit(a):
    return a//10000
print(first_digit(12345))
"""
#o/p--> 1

#12. Calculate Area of Rectangle
#Write a function that accepts length and breadth and returns the area.
#Area = length × breadth

"""
def area(length,breadth):
    print(length*breadth)
area(10,20)
"""
#o/p--> 200

#13. Calculate Simple Interest
#Write a function that accepts:
#principal
#rate
#time
#and returns simple interest.
#SI = (P × R × T) / 100

"""
def simp_intr(p,r,t):
    return (p*r*t)/100
print(simp_intr(2,3,4))
"""
#o/p--> 0.24

#14. Find Average of Three Numbers
#Write a function that accepts three numbers and returns their average.
"""
def average(a,b,c):
    return (a+b+c)/3
print(average(2,3,4))

o/p-->3.0
"""
#15.Count Vowels
#Write a function that accepts a string and returns the number of vowels.
#Input: "education"
#Output: 5
"""
def total_vowel(input):
    count=0
    for i in input:
        if i in "AEIOUaeiou":
            count=count+1
    print(count)
total_vowel("education")
"""
#o/p-->5

#16.Count Consonants
#Write a function that accepts a string and returns the number of consonants.
"""
def consonent(input):
    count=0
    for i in input:
        if i not in "AEIOUaeiou":
           count=count+1
           print(count)
consonent("education")
"""
#o/p--> 1
#           2
#           3
#           4

#17. Count Digits in a String
#Write a function that accepts a string and counts how many digits are present.
#Output: 4
"""
def digit(input):
    count=0
    for i in input:
        if i.isdigit():
            count=count+1
            print(count)
digit("abc123xy5")
"""
#o/p--> 1
#2
#3
#4

#18.. Reverse a String
#Write a function that accepts a string and returns the reversed string.
#Input: "python"
#Output: "nohtyp"

"""
def reverse(input):
    return input[::-1]
print(reverse("python"))
"""
#o/p--> "nohtyp"
"""
def reverse(input):
    for i in reversed (input):
        print(i,end=" ")
reverse("python")
"""
#O/P--> n o h t y p

#19.Return Only Positive Numbers
#Write a function that accepts a list and returns a new list containing only positive numbers.
"""
a = [10, -5, 20, -2, 30]

x=[]
def positive_num(a):
    for i in a:
        if i>0:
            x.append(i)
    return x
print(positive_num( [10, -5, 20, -2, 30]))
"""
#o/p--> [10, 20, 30]

#20.wap to perform addition and subtraction if "a" is greater than "b"
#return sum else return difference
"""
def operation(a,b):
    if (a>b):
        return a+b
    else:
        return a-b
print(operation(20,10))
print(operation(100,500))
"""
#o/p--> 30
#           -400

#21.waf to check string is palindrome or not (take user input)
"""
def check():
    a=eval(input("enter the string:->"))
    if a==a[::-1]:
          print("the given string is palindrome")
    else:
        print("the given string is not palindrome")
(check())
"""
#o/p--> enter the string:->"mom"
#              the given string is palindrome

#22.wap to return length of variable keywords arguments
"""
#(**KWARGS)
length=0
def  length_data(**kwargs):
    length=0
    global length
    for i in kwargs:
        print(i)
        length+=1
        print(length)
length_data(a=10,b=20,c=30,d="hello",e=[1,2,3])
"""
#23.wap to return length of the variable positional arguments
"""
length=0
def  length_data(*args):
    global length
    for i in args:
        print(i)
        length+=1
        print(length)
length_data(10,20,30,"hello",[1,2,3])
"""
#o/p-->
"""
10
1
20
2
30
3
hello
4
[1, 2, 3]
5
"""

#24.waf to search for character in a given string and return corresponding index
 # string="coding part is done"

#a= "coding part is done"
"""
def search_char(a):
    sub=eval(input("enter the substring:-->"))
    for i in range (len(a)):
        if a[i]==sub:
            print("character found:",sub,i)
search_char("coding part is done")      
"""
#o/p--> enter the substring:-->'e'
#            character found: e 18

#25.wap to squaring of the element in the given list

def sqr(num):
    newl=[]

    for i in num:
       # e=i**2  
        newl.append(i**2  )

    print(newl)

sqr([1,2,3,4])

#27.wap to read 3 numbers from the user,first two numbers should
#be added and the result of addition should be subtracted by third
#number.
    

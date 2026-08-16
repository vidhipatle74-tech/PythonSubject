#WAP to print python 5 times.
'''
i=1
while i<=5:
    print("Python")
    i+=1
#o/p-->
#       Python
#       Python
#       Python
#       Python
#       Python
'''
#WAP to print a natural number.
'''
i=1

while i<=10:
    print(i)
    i+=1
#o/p-->
        1
        2
        3
        4
        5
        6
        7
        8
        9
        10
'''

#WAP to print multiplication table for n.
'''
n=eval(input("enter the number:-"))
i=1

while i<=10:
    print(n,"*",i,"=",n*i)
    i+=1

#o/p-->
    enter the number:-2
                      2 * 1 = 2
                      2 * 2 = 4
                      2 * 3 = 6
                      2 * 4 = 8
                      2 * 5 = 10
                      2 * 6 = 12
                      2 * 7 = 14
                      2 * 8 = 16
                      2 * 9 = 18
                      2 * 10 = 20
'''

#WAP to run infinite loop until user enter the correct password.
'''
password="Vidhi#123"

while True:
    p=input("enter the password:")

    if p==password:
        print("password is correct")
        break
#o/p-->
       enter the password:Vidhi#123
       password is correct
'''

#WAP to find the sum of the natural numbers.
'''
n=eval(input("enter the number:"))
i=1
sum=0

while i<=n:
    sum=sum+i
    i+=1
print("sum=",sum)

#o/p-->
      enter the number:5
      sum= 15
'''

#WAP to find the  product of n  natural number  or factorial of the number.
'''
n=int(input("enter the number: "))
i=1
fact=1

while i<=n:
    fact=fact*i
    i+=1
print(fact)

#o/p-->
       enter the number: 5
       120
'''

#WAP to print all the character of the string.
'''
n=input("enter the string:")
i=0

while i< len(n):
    print(n[i])
    i+=1
o/p-->
enter the string:hello
                 h
                 e
                 l
                 l
                 o
'''

#WAP to print all the character present at even index of the string.
'''
n=input("enter the string:")
i=0

while i< len(n):
    print(n[i])
    i+=2

#o/p-->
       enter the string:hello
       h
       l
       o
'''

#WAP to extract all the lowercase characters present in a string.
'''
n=input("enter the string:")
i=0

while i<len(n):
    if n[i].islower():
         print(n[i])
    i+=1

#o/p-->
       enter the string:HeLlW wOrLd
       e
       l
       w
       r
       d
'''
#WAP to extract all the vowels present in a string.
'''
n=input("enter the string:")
i=0

while i<len(n):
    if n[i] in "aeiouAEIOU":
        print(n[i])
    i+=1
#o/p-->
        enter the string:HeLlW wOrLd
        e
        O
'''

#WAP to print factors of an integer number.
'''
n=int(input("enter the number:"))
i=1

while i <= n:
    if n%i==0:
        print(i)
    i+=1
#o/p-->
       enter the number:7
       1
       7
'''

#WAP to toggle a string.
'''
s = input("Enter a string: ")

i = 0
result = ""

while i < len(s):
    if s[i].islower():
        result += s[i].upper()
    else:
        result += s[i].lower()
    i += 1

print("Toggled string:", result)

#o/p-->
       Enter a string: hello world
       Toggled string: HELLO WORLD
'''

#WAP to reverse the given number.
'''
n = int(input("Enter a number: "))

rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reverse number:", rev)

#o/p-->
      Enter a number: 3456
      Reverse number: 6543
'''
#WAP to find the sum of individual digits of a number.
'''
n = int(input("Enter a number: "))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

print("Sum of digits:", sum)

#o/p-->
       Enter a number: 45
       Sum of digits: 9
'''

#WAP to check whether the number is perfect or not.

n = int(input("Enter a number: "))

i = 1
sum = 0

while i < n:
    if n % i == 0:
        sum = sum + i
    i += 1

if sum == n:
    print("Perfect number")
else:
    print("Not a perfect number")

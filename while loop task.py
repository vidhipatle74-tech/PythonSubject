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
'''
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

o/p-->
       Enter a number: 5
       Not a perfect number
'''
#wap to login to phonepay to enter the correct otp
'''
correct_otp = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    otp = input("Enter OTP: ")

    if otp == correct_otp:
        print("Login successful")
        break
    else:
        attempts += 1
        print("Incorrect OTP")

if attempts == max_attempts:
    print("Too many wrong attempts. Login failed.")

#o/p-->
    Enter OTP: 1234
    Login successful
'''
#wap to extract all the even integer present in the  tuple at odd index.
'''
t = (10, 15, 22, 35, 40, 51, 60, 75)
i = 1

while i <=len(t):
    if t[i] % 2 == 0:                #remaining ans is showing blank space
        print(t[i])
    i += 2
'''

#WAP to remove duplicates from a list without converting into set.
'''
l = [10, 20, 10, 30, 20, 40, 30]

new = []
i = 0

while i < len(l):
    if l[i] not in new:
        new.append(l[i])
    i += 1

print(new)

#o/p-->
       [10, 20, 30, 40]
'''

#WAP to find the sum of all the odd numbers between the given range.
'''
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

sum = 0

while start <= end:
    if start % 2 != 0:
        sum = sum + start
    start += 1

print("Sum of odd numbers =", sum)

o/p-->
      Enter starting number: 3
      Enter ending number: 5
      Sum of odd numbers = 8
'''
#WAP to find the greatest number in a given list of integers.
'''
l = [10, 25, 7, 45, 18, 32]

i = 0
greatest = l[0]

while i < len(l):
    if l[i] > greatest:
        greatest = l[i]
    i += 1

print("Greatest number =", greatest)

#o/p--> Greatest number = 45
'''
#WAP to find the sum of cube of a number in a string.
'''
s = "12345"

i = 0
sum = 0

while i < len(s):
    if s[i].isdigit():
        n = int(s[i])
        sum = sum + n ** 3
    i += 1

print("Sum of cubes =", sum)

#o/p--> Sum of cubes = 225
'''

#WAP to check whether the number is Armstrong or not.
'''
n = int(input("Enter a number: "))

temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** 3
    n = n // 10

if sum == temp:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

#o/p--> Enter a number: 153
        Armstrong number
'''

#1.wap to check a data is a sequence/iterable/individual data type.
'''
from collections.abc import Iterable,Sequence
data=eval(input("enter the data"))

if isinstance(data,Sequence) and not isinstance(data,(str,bytes)):
    print("the data is a Sequence")

elif isinstance(data,Iterable):
    print("The data is an Iterable")

else:
    print("The data is Individual")
'''

#3.wap if input is string return its length,else if input is list pop element,else if
#input is tuple reverse else invalid input.

'''a=eval(input("enter the data"))
if input(str):
    print("len(a)")

elif input(list):
    print("a.pop()")

elif input(tuple):
    print("a.reverse")

else:
    print("invalid input")'''

#4.wap to check a age belongs to category 0 to 17 child and 18 to 30 ur adult,31 to 60 ur men,
#61 to 100 senior citizen,else invalid

'''age=eval(input("enter the age"))
if age<17:
    print("child")

elif 18<=age<=30:
    print("you are adult")

elif 31<=age<=60:
    print("you are men")

elif 61<=age<=100:
    print("senior citizen")

else:
    print("invalid age")'''

#wap to take marks of 5 sub,calculate the average if the average is b/w 90-100 print Distinction
#if 75-89 print first class and if it's 60-74 print second class, if 50-59 print Third class,below 50 is fail
#note:-->max marks is 100

'''
marks=eval(input("enter the average"))

if 90<=marks<=100:
    print("Distinction")

if 75<=marks<=89:
    print("First class")

if 60<=marks<=74:
    print("Second class")

if 50<=marks<=59:
    print("Third class")

if marks<50:
    print("Fail")
'''

#WAP to check whether a given number is divisible by 3 and 5. If the number is divisible by 3 print Fizz,
#if the number divisible by 5 print 'buzz' if it divisible by both then print fizz buzz 
'''
num=eval(input("enter the number"))

if num/3:
    print("Fizz")                          #output fizz hi aara h 

elif num/5:
    print("buzz")

elif num/(3,5):
    print("fizz buzz")

'''
    
#WAP to check if a given number is one digit or two digit or three digit or more than 3 digit.
#If one digit display the one digit, if two digit display the two digit value and so on. 
'''
num=eval(input("enter the number"))

if num<=9:
    print("number is one digit value")

elif num<=99:
    print("number is two digit value")

elif num<=999:
    print("number is three digit value")

else:
    print("more than three digit")

'''

#WAP to accept any number from 1-5 and display that number is word form
'''
num=eval(input("enter the int number"))

if num==1:
    print("one")

elif num==2:
    print("Two")

elif num==3:
    print("Three")

elif num==4:
    print("Four")

elif num==5:
    print("Five")

else:
    print("none")
'''
#------------------------------------------------------------------------------------------------------------------
#WAP to check whether a given character is uppercase or lowercase or special character.
#if uppercase convert to lowercase or leif lowercase, conver into upper or else display the
#[revious, given and next characters and display it.]

#-------------------------------------------------------------------------------------------------------------------
'''a=eval(input("enter the char"))

if 65<=a<=90:
    a.isupper()
    print("uppercase")'''
    
#wap  to check given Password length is lessthan 6 print week and length is in between 6 to 8 medium
#else password length is 9 to 12 strong above print verystrong
'''
password=eval(input("enter the length"))

if password<6:
    print("week")

elif 6<=password<=8:
    print("medium")

elif 9<=password<=12:
    print("strong")

else:
    print("very strong")
'''

#Create a Login System:
#Correct username and password → Login Successful
#Correct username, wrong password → Incorrect Password
#Wrong username → User Not Found

correctusername=eval(input("enter the username"))
correctpassword=eval(input("enter tha password"))
wrongpassword=eval(input("enter the  password"))
correctusername==password=eval(input("enter the password"))
correctusername==wrong password=eval(input("enter the password"))

if username and password==correct:
    print("Login Successfull")

elif username==correct & password==wrong:
    print("Incorrect password")

elif username==wrong:
    print("user not found")

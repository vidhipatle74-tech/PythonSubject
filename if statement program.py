Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #wap the program to check the given string is in lowercase or not.
>>> 
>>> a='HELLO'
>>> if a.isupper():
...     print('uppercase data')
... 
...     
uppercase data
>>> 
>>> #wap the program to check the given string is in lowercase or not.
>>> 
>>> a='hello'
>>> if a.islower():
...     print('lowercase data')
... 
...     
lowercase data
>>> #wap the program to check the given string contain number or not.
>>> 
>>> c='12345678'
>>> if a.isdigit():
...     print("it's a digit")
... 
...     
>>> 
>>> 
>>> c='12345678'
>>> if c.isdigit():
...     print("it's a digit")

    
it's a digit

#without inbuilt function;;

#wap the program to check the given string is in uppercase or not.
a='HELLO'
if ord('A')<=ord(x)<=ord('Z')
SyntaxError: expected ':'
if ord('A')<=ord(x)<=ord('Z'):
        print("uppercase data")

        
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    if ord('A')<=ord(x)<=ord('Z'):
NameError: name 'x' is not defined
x='HELLO'
if ord('A')<=ord(x)<=ord('Z'):
        print("uppercase data")

        
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    if ord('A')<=ord(x)<=ord('Z'):
TypeError: ord() expected a character, but string of length 5 found






#wap to check the given character is lowercase then convert to uppercase.

a="goodmorning"
if a.islower():
    a=a.upper()
    print(a)

    
GOODMORNING

a="Good morning123*&"
if a.islower():
    a=a.upper()
    print(a)

    






e="H"
if ord("A")<=ord(e)<=ord("Z"):
    print(chr(ord(e)+32))

    
h

#wap the program to convert uppercase to lowercase character.

e="B"
if ord("A")<=ord(e)<=ord("Z"):
    print(chr(ord(e)+32))

    
b

#wap the program to convert lowearcase to uppercase.

e='h'
if ord("a")<=ord(e)<=ord("z"):
    print(chr(ord(e)+-32))

    
H
#if you want to convert the lowercase  character to uppercase character then you need to use (-32)

#if ord("a")<=ord(e)<=ord("z"):
    #print(chr(ord(e)+-32))

#if you want to convert the uppercase  character to lowercase character then you need to use (+32)

#if ord("A")<=ord(e)<=ord("Z"):
  #  print(chr(ord(e)+32))
  


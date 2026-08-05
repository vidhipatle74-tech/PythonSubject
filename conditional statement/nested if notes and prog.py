#NESTED IF STATEMENT:

#if statement inside another if statement is known as nested if statement.

#STNTAX:
#        if <condition1>:
#       |
#       |       if <condition2>:
#       |       |
#       |       |       if <condition3>:
#       |       |       |
#       |       |       |
#       |       |      else:--(FSB)
#       |       |
#       |       |
#       |       else:--(FSB)
#       |
#       else:-->(FSB)


#wap a program to check the middle vowel in a list is string or not.
'''
ls=eval(input("enter the list:"))

if len(ls)%2==1:

      if type(ls[len(ls)//2])==str:
        print("the middle is string")

      else:
           print("the middle value is not string")

else:
    print("the length is even and no middle value")
'''


#wap program to check whether the character is vowel or not.
'''
ch=(input("enter the char:"))

if ch.isalpha():
    if ch in 'AEIOUaeiou':
        print("char--> is a vowel")

    else:
            print("char--> is consonents")
else:
    print("char--> is not alphabet")
'''

#wap to check whether the last value is a list is palindrom or not and start with vowels or not.

'''
a=eval(input("enter the list data"))

if a[-1]==a[-1][::-1]:
    if a[-1][0] in 'AEIOUaeiou':
        print("a[-1]-->is palindrome and starts with vowels")

    else:
        print("a[-1]-->is palindrome and starts with consonents")

else:
    print("last value is not a palindrome....")
'''

#wap to check the instagram username or password.
'''
username=eval(input("enter the username"))
password=eval(input("enter the password"))
p_w='1234'
u_n='vidhi'

if username==u_n:
    if password==p_w:
        print("login successful")

    else:
        print("invalid pasword")
else:
    print("user not found")
'''

#wap a program to find greatest of four number
'''
a=eval(input("enter the number"))
b=eval(input("enter the number"))
c=eval(input("enter the number"))
d=eval(input("enter the number"))

if  a>b:
    if a>c:
        if a>d:
            print("the number {a} is greatest")
        else:
            print("the number {d}is greatest")

    else:
     if c>d:
        print("the number {c} is greatest")

     else:
        print("the number {d} is greatest")
else:
    if b>c:
        if b>d:
            print("the number {b} is greatest")
        else:
            print("the number {d} is greatest")

    else:
        if c>d:
            print("the number {c} is greatest")

        else:
            print("the number {d} is greatest")
    '''

#wap to craete menu drive

ls=eval(input("enter the data"))
if type (ls)==list:
    print('1-->pop()')
    print('2-->append()')
    print('3-->clear()')

    choice=int(input("enter the choice"))
    if choice==1:
        ls.pop()
        print(ls)
        
    elif choice==2:
          data=eval(input("enter the data"))
          ls.append(data)
          print(ls)

    elif choice==3:
          ls.clear()
          print(ls)

    else:
        print("invalid choice")

else:
    print(" entered data is not a list ")


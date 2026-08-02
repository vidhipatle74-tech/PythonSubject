#NESTED IS STATEMENT:

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

ls=eval(input("enter the list:"))

if len(ls)%2==1:

      if type(ls[len(ls)//2])==str:
        print("the middle is string")

     else:
    print("the middle value is not string")

else:
    print("the length is even and no middle value")

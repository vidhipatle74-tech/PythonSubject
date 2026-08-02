
#IF_ELSE:

#if the given condition is true it will execute, in true state block ,
#but if the given condition  is  becomes false it will wait and won't show blank space , it will  execute in false state block (else block)

#SYNTAX:-->> if condition:

#             statement( TSB)      #TRUE STATEMENT BLOCK
#              .
#              .
#              else:
#                   statement(FSB)   #FALSE STATEMENT BLOCK


 

#FLOWCHART:

                               #START
                                  #|
                                #CONDITION--->> EXPRESSION-->> TRUE/FALSE
                                  #|
            #TRUE                                      #FALSE
             #|                                           #|
        #TRUE STATE BLOCK                        #FALSE STATE BLOCK



#WAP the program to check the given number is even

#a=67
##WAP the program to check the given number is even or odd


#write a program to checck the password id matching or not.
#user input

'''user=eval(input("enter the Name"))
password=eval(input("enter the Password"))


if user=="PYthon" and password=="PY":
    print("Both username and password not matching")

else:
    print("Both username and Password not matching")
'''


#s={1:2,4:5,8:9}

#wap to check the given dictionary length  is even print as it is  , else add one
#key and value pair make it as a given

s={1:2,4:5,8:9}

if len(s)%2==0:
    print(s)

else:
    s[100]="HII"
print(s)




#wap the program to check the given number is odd  if it is odd print as it is
#else if it is even convert it into negative.

num=eval(input("enter the number :"))

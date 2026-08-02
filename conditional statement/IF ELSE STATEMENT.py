Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
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

a=67
##WAP the program to check the given number is even or odd


#write a program to checck the password id matching or not.
#user input

user=eval(input("enter the Name"))
password=eval(input("enter the Password"))


if user=="PYthon" and password=="PY":
    print("Both username and password not matching")

else:
    print("Both username and Password not matching")

    

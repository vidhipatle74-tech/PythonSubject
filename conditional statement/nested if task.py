#wap the program to check the given number is even and greater than 5
'''
num=eval(input("enter the number"))
if num%2==0:
    print(f'the given number is {num}  is even')

    if num>5:
          print(f'the number {num}  is greater')
    else:
        print(f'the given number {4}  is lesser')

else:
    print(f'the given number {num} is odd')
 '''   

#2.wap to check the number is odd and check if the number is divisible by 7
#n=35
'''
num=eval(input("enter the number"))

if num%2==1:
    print(f'the given number {num} is odd')

    if num%7==0:
        print(f'the number {num}is divisible by 7')

    else:
        print(f'the number {num} is not divisible by 7')
else:
    print(f'the given number {num} is even')

'''

#3.wap to check the number is odd and check if the number is divisible by 7
#n=33


#4.wap to validate facebook username and password
#condition is:---> username-->"python"  and password="python masters"
'''
FB_user_name=eval(input("enter the username"))
if FB_user_name=="python":
    print("usernme is valid")
    
    password=eval(input("enter the password"))

    if password=="python master":
        print("password is valid")

    else:
        print("password is invalid")
else:
    print("username is invalid")
'''

#9.wap to perform list operations user should enter only list data type,if options 1 pop().
#options 2 sort() options 3 clear() invalid options,invalid data type.
'''
data=eval(input("enter the data type"))

if isinstance(data,list):
    print("yes we are passing only list datatype")

    option=eval(input('enter the option(1,2,3)'))

    if option==1:
        data.pop()
        print(data)

    elif option==2:
        data.sort()
        print(data)

    elif option==3:
        data.clear()
        print(data)
    else:
        print("invalid datatype")

else:
    print("we are not pasing list datatype")

'''
#upper to lower, lower to upper , swapcase, capitalize.

'''
data=eval(input("enter the datatype"))
if isinstance(data,str):
    print("yes we are passing string datatype")

    option=eval(input("enter the options(1,2,3,4)"))

    if option==1:
        data.upper()
        print(data)

    elif option==2:
        data.lower()
        print(data)

    elif option==3:
        data.swapcase()
        print(data)

    elif option==4:
         data.capitalize()
         print(data)
    else:
        print("invalid datatype")

else:
    print("we are not  passing  string datatype")
'''

#.wap to Book ticket in Book my show

#condition:---> first it should ask theaters name then it should display the movie available
 #                         then it has to display ticket price and in the end ticket should be booked


theatre=["pvr","INOX","CINELPOIS"]
user=eval(input("enter the theatre name"))

if user in theatre:
    print(f'user is selected to the{theatre}')

    movies=["RRR","KGF","ANIMAL","RAVAN"]
    user1=eval(input("enter the movie name"))

    if user1 in movies:
        print(f'here {user} is selected to the theatre and {user1} is selected to the movie')
    
        ticket_price=[1000,2000,3000,4000]
        amount=eval(input("enter the amount"))
        
        if amount==ticket_price[0]:
            print(f'here user is {user} selected the theatre name and {user1} is selected for movie and ticket_price is {amount}')

        elif amount==[1]:
            print(f'here user is {user} selected the theatre name and {user1} is selected for movie and ticket_price is {amount}')
        elif amount==[2]:
            print(f'here user is {user} selected the theatre name and {user1} is selected for movieand ticket_price is {amount}')
        elif amount==[3]:
            print(f'here user is {user} selected the theatre name and {user1} is selected for movie and ticket_price is {amount}')
        elif amount==[4]:
            print(f'here user is {user} selected the theatre name and {user1} is selected for movie and ticket_price is {amount}')
        else:
            print("ticket_price is to low")
    else:
        print("wrong movie selected")
else:
    print("wrong theatre selected")



#7.wap to purchase a phone from the shopping app
#apps=[“flipkart”,”amazon”]
#categories=[“electronics”,”mobile”,”fashion”,”furnitures”]

app=eval(input("enter the app"))
user=eval(input("enter the user"))

if user in apps:
    print(f'user purchase product from app')
    
    apps=["flipkart","Amazon"]
    user1=eval(input("enter the app name"))

    if user1 in apps:
        print(f'here {user} is selected to app and {user1} is purchase product from app')

        phone_price=[15000,25000,35000,45000]
        amount=eval(input("enter the amount"))

        if amount=
        
        
    


#8.wap to give 10% off only who is purchasing in credit card and min 3 product should purchase and
#each product price should be more than 500




#9.wap to perform list operations user should enter only list data type,if options 1 pop().
#options 2 sort() options 3 clear() invalid options,invalid data type

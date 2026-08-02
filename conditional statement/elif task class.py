###wap to check the given number is +ve/-ve/0 ####

'''num=eval(input("enter the number"))
if num>>0:
    print("its a positive numbre")

elif num==0:
    print("neutral number")

if num<0:
    print("its a negative number")

elif num==0:
    print("neutral number")



###wap to check the given character is alphabet or digit or special character.###

chr=eval(input("enter the character"))
if chr.isalpha():
    print("its a alphabet")

elif chr.isdigit():
    print("itsb a digit")

else:
    print("its a special character")


###wap to check the given character is uppercase/lowercase/digit.with and without using inbuilt function#####

v=eval(input("enter the characgter"))
if ord("A")<=ord(v)<=ord("Z"):        #65<=character<=90 -->condition to find uppercase character between that numbers
    print("its a uppercse")

elif ord("a")<=ord(v)<=ord("z"):
    print("its a lowercase")

elif ord("0")<=ord(v)<=ord("9"):
    print("its a digit")

#####wap to print based on number print day name######


num=eval(input("enter the number"))

if num==1:
    print("monday")

elif num==2:
    print("tuesday")

elif num==3:
    print("wednesday")

elif num==4:
    print("thursday")

elif num==5:
    print("friday")

elif num==6:
    print("saturday")

elif num==7:
    print("sunday")

else:
    print("invalid number8")'''

#wap to perform based on the opertors symbol take user inputs .

'''a=eval(input("enter the number--"))
b=eval(input("enter the number--"))
operator=eval(input("enter the symbol--"))

if operator=="+":
    print(a+b)

elif operator=="-":
    print(a-b)

elif operator=="*":
    print(a*b)

elif operator=="/":
    print(a/b)

elif operator=="//":
    print(a//b)

elif operator=="%":
    print(a%b)

elif operator=="**":
    print(a**b)

else:
    print("invalid number")

#wap to check the greater number among three numbers

x=eval(input("enter the number"))
y=eval(input("enter the number"))
z=eval(input("enter the number"))

if x>y and x>z:
    print(x)

elif y>x and y>z:
    print(y)
  
elif z>x and z>y:
    print(z)


#wap to check the  smallest number among three number.

x=eval(input("enter the number"))
y=eval(input("enter the number"))
z=eval(input("enter the number"))

if x<y and x<z:
    print(x)

elif y<x and y<z:
    print(y)
  
elif z<x and z<y:
    print(z)

'''

#wap to check the ------------------------

age=eval(input("enter the number"))

if age<17:
    print("children marriage")
    
elif age==18:
    print("eligible for marriage")

elif 18<=age<=25:
    print("eligible for love marriage")

elif 25<=age<=30:
    print("arrange marriage")

elif 30<=age<=40:
    print("your wish")



#2.wap to check a data is a sequence/iterable/individual data type.

data=eval(input("enter the data"))

    

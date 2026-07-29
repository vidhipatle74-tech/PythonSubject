'''(1)Ravi would like to buy a new cello or red pen. The cost of the pen should be 10.
If the pen is available in the shop, he will buy the pen. If it is not there he will
come out of the shop.

pen_available=eval(input("enter YES/NO"))
pen_price=eval(input("enter the amount"))

if pen_available=="yes" and pen_price==10:
    print(f'ravi will buy the pen')

else:
    print(f'ravi will come out to the shop')'''


'''(2)WAP to perform addition and subtraction operation by using list collection if the
first and middle data items number are even performing addition operation, or
else performing subtraction.

a=[10,20,30,47,50,60,70]
low=0
high=len(a)-1
first_element=a[0]    #var_name[position]
print(first_element)
mid_element=(low+high)//2   #mid=(low+high)//2
print(mid_element)
print(a[mid_element])

if first_element%2==0 and a[mid_element]%2==0:
    print(first_element+a[mid_element])

else:
    print(first_element-a[mid_element])'''


'''(3)WAP to check whether the first item of these two lists is either integer or not.
If it is an integer, concatenate these two lists or else print the memory
address of these two lists.'''

a=[10,20,30,40]
b=[5,6,7,8,9]

if isinstance(a[0],int) and isinstance(b[0],int):
    print(a[0]+b[0])
else:
    print(f'first list id-->',id(a))
    print(f'second list id-->',id(b))
    


'''(4)WAP to check whether a given value is less than 125 and in between 47 to 125 or
not. if condition is True, to perform store the given value as key and value as a
character into the dict or else to append the value in list and display it.

num=eval(input("enter the number"))
d={}
l=[]
if num<125 and 47<=num<=125:
    d[num]=chr(num)
    print(d)
else:
    l.append()
    print(l)'''



'''WAP to check whether the given string of the first character is a special symbol
or not. If a special symbol, to extract and display the middle character or else to
reverse the string and display the half of the string'''

a=eval(input("enter the data"))
mid=(len(a)-1)//2

if not a[0].isalnum():
    print(mid,a[mid])
else:
    rev=a[::-1]
    print(rev[0:mid+1:1])


'''WAP to check whether a given character is a vowel or consonant. if vowel,to
print the next character of a given character or else print previous characters.


a=eval(input("enter the data"))
if a in "AEIOUaeiou":
    print()'''#remaining


'''WAP to check whether a given string is less than 3 characters, to print the entire
string otherwise to print after third positions to the remaining string.

num=eval(input("enter the data"))'''


'''WAP to check whether a given length of the string is even or not. if even, to
append the new string called "bye" or else print the first and last characters.'''

s=eval(input("enter the data"))
if len(s)%2==0:
    print(s+""+"bye")

else:
    print("first character-->",s[0])
    print("second character-->",s[-1])


'''WAP to check whether the last of the given string is a special character or not, if
the special character prints reverse the string except the last character or else to
check if the length of the string is odd or not, if odd to extract the middle
character to the end of the string'''

a=eval(input("enter the data"))
if not a[-1].isalnum():
    rev=a[::-1]
    print(rev)
    print(rev[-2::-1])

else:
    if len(a)%2==1:
        mid=(len(a)-1)//2
        print(mid)
        print(a[mid])


'''WAP whether a given string, if string length is more than 2, then it displays a new
string with the first and last characters switched, otherwise the display the 3
copies of given string.'''




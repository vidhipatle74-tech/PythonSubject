'''WAP to check whether a given value is a list and first and last values should be
integer if condition is satisfied first value is True division by 3 and perform the
bitwise not for last value and those result values are stored in same positions in
given list or else, to perform length of the collection power by 2 and display
value.


#WAP to check whether a given value is a list and first and last values should be\ninteger if condition is satisfied first value is True division by 3 and perform the\nbitwise not for last value and those result values are stored in same positions in\ngiven list or else, to perform length of the collection power by 2 and display\nvalue.'

a=[1,"ab",8.9,True,5]
if isinstant(a_list) and isinstance(a[0],int) and isinstance(a[-1],int):
   a[0]=a[0]/3
a[-1]=~a[-1]/3
   print(a)
else:
    print(len(a)**2)'''
    

'''WAP to check whether a given value is a string or not and length of the value
should be more than 7, if condition is satisfied to append the new string in the
middle of the given string or else to perform the replications with 3 and display
the result.

a=eval(input("enter the data"))
low=0
high=len(a)-1
if isinstance(a, str) and len(a)>7:
    sub_string=eval(input("insert the data"))
    mid=(low+high)//2
    print(mid)

#
a=eval(input("enter the data"))
low=0
high=len(a)-1
if isinstance(a, str) and len(a)>7:
    sub_string=eval(input("insert the data"))
    mid=(low+high)//2
    data=a[:mid:]+sub_string+a[:mid:]
    print(data)
else:
    print(a*3)

#---------------------------------------------------------------------------------------------------------------------
d="Morningclass"
e="777"


if type(d)==str and len(d)>7:
    print(d)
    insert="777"
    mid=len(d)//2
    print(mid)     #mid position
    print(d[mid])    #middle character
    final_res=d[0:mid:1]+insert+d[mid+1::]
    print(final_res)
else:
    print(d*3)'''


'''WAP to check if the given string of first and second character should be sequence
or not. if the sequence prints the first, second and last two characters, or else the
first half string is reversed and the remaining half string should be normal and
display it.


x=eval(input("enter the data"))
low=0
high=len(x)-1
if (ord("x")+1)==ord("b"):
    print("first_character-->",x[0])
    print("second_character-->",x[1])
    print("last_two character-->",x[-1,-2])

    
else:
    mid=(low+high)//2
    print(mid)
    data=x[0:mid+1][::-1]+x[mid+1::]
    print(data)'''




'''WAP to check whether a given collection is set or not. if set, append the new
value, or else eliminate the duplicate values in collection. final results should be
set type.

#case--1-->

a=eval(input("enter the data type"))
if isinstance(a,set):
    new_value(input("enter the elements"))
    a.add(new_value)
    print(a)
else:
    u=set(a)
    print(u)'''

'''WAP to check whether a given value is even and in between 65 to 90 and not in
0 or odd. if condition is True, to perform display the ascii character or else to
perform floor division with 5 and display it.


a=eval(input("enter the data"))'''


'''WAP to check whether a given string collection is more than ten, and the first +
last character of the ascii values should be divisible by 5, if condition is satisfied
print first, middle, last characters ASCII values or else print the string three
times'''



    
'''WAP to print the string collection five times when the length of the string
collection should be more than 3 and the middle character of the string should
be vowel and the first character ASCII value should be even, to print the previous
character of middle character, or else if ASCII value is odd then print the string
three times as print that string.'''


x=eval(input("enter the data"))
low=0
high=len(x)-1
mid=(low+high)//2
if len(x)>3 and x[mid] in "aeiouAEIOU" and ord(x[0])%2==0:
    print(chr(ord(x[mid])-1))
else:
    print(x*3)
    

# find the factorial for the given number.
'''
num=eval(input("enter the number:"))
i=1
out=[]
while i<=num:
    if num%i==0:
        out.append(i)
    i+=1
print(out)

#o/p-->
       enter the number:28
       [1, 2, 4, 7, 14, 28]
  
'''

#wap to find perfect number.
'''
num=int(input("enter the number:"))
i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+1
    i+=1

if sum==num:
    print("the number is perfect")
else:
    print("the numberb is not perfect number")
print(num)

#o/p-->
#     enter the number:10
#     the number is not perfect number
#     10
 
'''
#wap to print prime number.
'''
num=int(input("enter the number:"))
i=1
out=[]

while i<=num:
    if num%i==0:
        out.append(i)
    i+=1
if len(out)==2:
    print("prime number")
else:
    print("its not a prime number")

#o/p-->
#    enter the number:7
#    prime number

#o/p-->
#    enter the number:9
#    its not a prime number
'''

#wap to check the number is armstrong or not.
'''
num=int(input("entre the number"))
dum=num
num_len=len(str(num))
out=0

while num>0:
    l_d=num%10
    out+=l_d**num_len
    num//=10
if out==dum:
    print("ita a armstrong")
else:
    print("its not a armstrong")

#o/p-->
#      entre the number:153
#      ita a armstrong
'''

#disarium  number.
'''
num=int(input("entre the number:"))
dum=num
num_len=len(str(num))
out=0

while num>0:
    l_d=num%10
    out+=l_d**num_len
    num_len-=1
    num//=10
if out==dum:
    print("ita a disariem number")
else:
    print("its not a disarium number")

#o/p-->

#      entre the number135
#      ita a disariem number
'''

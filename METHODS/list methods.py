Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#COPY()

# it is nothing but it will copying from one variable to another variables

#SYNTAX:     new var_name= old var_name

#NOTE:    in normal copy/ copy both variable id address should be same .


a=[10,20,30,40]
b=a
a
[10, 20, 30, 40]
b
[10, 20, 30, 40]

id(a)
1870351726464
id(b)
1870351726464


#MODIFICATION IN VARIABLE:

#append()----->var_name.append(element)
a.append(100)
a
[10, 20, 30, 40, 100]
b
[10, 20, 30, 40, 100]


#MODIFICATION IN B VARIABLE:

#insert-----> var_name.insert(position,value)
b.insert(3,50)
b
[10, 20, 30, 50, 40, 100]
a
[10, 20, 30, 50, 40, 100]

#MODIFICATION IN VARIABLE WITHOUT USING USING INBUILT FUNCTION :

#var_name[position]=value

a
[10, 20, 30, 50, 40, 100]
a[1]
20
a[1]="Good"
a
[10, 'Good', 30, 50, 40, 100]
a[5]="Unique"
A
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    A
NameError: name 'A' is not defined. Did you mean: 'a'?
a[5]
'Unique'
a
[10, 'Good', 30, 50, 40, 'Unique']



                        #SHALLOW COPY():

#it will copying form one variable to another variable

#SYNTAX:     new var_name=old var_name.copy()

#both variable id address should be different ,because of this copy model.




#CASE 01:---->

x=["abc","xyz","mno","pqr"]

y=x.copy      # normal copy
y=x.copy
x
['abc', 'xyz', 'mno', 'pqr']
y
<built-in method copy of list object at 0x000001B379A50940>
y=x.copy()
x
['abc', 'xyz', 'mno', 'pqr']
y
['abc', 'xyz', 'mno', 'pqr']


id(x)
1870351632704
id(y)
1870351632064


#MODIFICATION IN X VARIABLE :

x
['abc', 'xyz', 'mno', 'pqr']

#syntax-----> var_name[position]=value

x[1]
'xyz'
x[1]=100
x
['abc', 100, 'mno', 'pqr']
y
['abc', 'xyz', 'mno', 'pqr']


#MODIFICATION IN Y VARIABLE :

y
['abc', 'xyz', 'mno', 'pqr']

#syntax:----> var_name[position]=value

y[0]=100
y
[100, 'xyz', 'mno', 'pqr']
x
['abc', 100, 'mno', 'pqr']


#CASE 02:----> NESTED LIST----> LIST INSIDE THE LIST

#we do modification in nested list it will affected on abother one --->case1
#we do modification in nested list it will affected on abother one --->case1  not affected in outside the nested list


k=[1,2,3,[10,20,30]]
l=k.copy()
k
[1, 2, 3, [10, 20, 30]]
l
[1, 2, 3, [10, 20, 30]]


#COMPLETE LIST ID ADDRESS----> id(var_name)

id(k)
1870306602880
id(l)
1870351790848


#NESTED LIST ID ADDRESS---->id (var_name[position])
id(k[3])
1870350708928
id(l[3])
1870350708928


#MODIFICATION OF K VARIABLE:

K
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    K
NameError: name 'K' is not defined. Did you mean: 'k'?
k
[1, 2, 3, [10, 20, 30]]
l
[1, 2, 3, [10, 20, 30]]
l
[1, 2, 3, [10, 20, 30]]



#MODIFICATION OF L VARIABLE:

l
[1, 2, 3, [10, 20, 30]]

l[0]=100
l
[100, 2, 3, [10, 20, 30]]
k
[1, 2, 3, [10, 20, 30]]
#beacuse both variable id address is different

#MODIFICATION IN NESTED LIST:
#-----> var_name[position]=value


k[3]
[10, 20, 30]
k[3][0]
10
k[3][0]="abc"
k
[1, 2, 3, ['abc', 20, 30]]

l
[100, 2, 3, ['abc', 20, 30]]



#NESTED LIST MODIFICATION IN L VARIABLE:

k
[1, 2, 3, ['abc', 20, 30]]
l[3]
['abc', 20, 30]
l[3][2]
30
l[3][2]="pyhton"
k
[1, 2, 3, ['abc', 20, 'pyhton']]
l
[100, 2, 3, ['abc', 20, 'pyhton']]


w=[100,500"walmart",["a","b","c","d"]]
SyntaxError: invalid syntax. Perhaps you forgot a comma?

w=[100,500,"walmart",["a","b","c","d"]]
n=w.copy()
w
[100, 500, 'walmart', ['a', 'b', 'c', 'd']]
n
[100, 500, 'walmart', ['a', 'b', 'c', 'd']]

#COMPLETE LIST ID ADDRESS:

 

id(w)
1870351835776
id(wn)
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    id(wn)
NameError: name 'wn' is not defined. Did you mean: 'w'?
id(n)
1870351632768


#NESTED LIST ID ADDRESS:

id(w[3])
1870351835904
id(n[3])
1870351835904




#,odification in outside the nested list:

w
[100, 500, 'walmart', ['a', 'b', 'c', 'd']]
w[1]
500
w[1]="snap"
w
[100, 'snap', 'walmart', ['a', 'b', 'c', 'd']]
n
[100, 500, 'walmart', ['a', 'b', 'c', 'd']]
n[1]
500
n[1]="snap"

n
[100, 'snap', 'walmart', ['a', 'b', 'c', 'd']]



w
[100, 'snap', 'walmart', ['a', 'b', 'c', 'd']]
n
[100, 'snap', 'walmart', ['a', 'b', 'c', 'd']]


w[3]
['a', 'b', 'c', 'd']

w[3][2]
'c'
w[3][2]="GOOD MORNING"
W
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    W
NameError: name 'W' is not defined. Did you mean: 'w'?
w
[100, 'snap', 'walmart', ['a', 'b', 'GOOD MORNING', 'd']]


n[3]
['a', 'b', 'GOOD MORNING', 'd']
w[3][2]="GOOD eveaning"
w
[100, 'snap', 'walmart', ['a', 'b', 'GOOD eveaning', 'd']]



w
[100, 'snap', 'walmart', ['a', 'b', 'GOOD eveaning', 'd']]
n
[100, 'snap', 'walmart', ['a', 'b', 'GOOD eveaning', 'd']]





             #DEEP COPY()

#it will copying from one variable to another variable
#step1--->

from copy import deepcopy

#SYNTAX---> new var_name=deepcopy(old var_name)

 #CASE01----->
c=[10.100,200,300]
e=deepcopy(c)

c
[10.1, 200, 300]
e
[10.1, 200, 300]

id(c)
1870351879232
id(e)
1870351834368
 # everything it will independently ,
 
#MODIFICATION OF C VARIABLE:
 
c
[10.1, 200, 300]
c[0]=9000
c
[9000, 200, 300]

e
[10.1, 200, 300]
e[0]="a"
e
['a', 200, 300]
c
[9000, 200, 300]

#both variable id address should be different


#CASE02--->

from copy import deepcopy

r=[10,20,30,40,["a","b","c","d"]]
u=deepcopy(r)

r
[10, 20, 30, 40, ['a', 'b', 'c', 'd']]


#complete list id addresss:

id(r)
1870351842624
id(u)
1870351790656


#nested list id addresss:
id(r)
1870351842624
id(u)
1870351790656
r
[10, 20, 30, 40, ['a', 'b', 'c', 'd']]









ord("A")
65
ord("B")
66

ord("C")
67
ord("Z")
90


ord("a")
97
ord("b")
98
ord("c")
99
ord("z")
122


ord("0")
48
ord("1")
49
ord("2")
50
ord("3")
51
ord("9")
57




chr(65)
'A'
chr(122)
'z'
chr(97)
'a'




#SORT():

#IT WILL EXCEPT HOMOGENIUS TYPE OF DATA
#BYDEFAULT IT WILL CONVERT LOWER NUMBER TO BIGGER NUMBER(ASCENDING TO DESCENDING)

#SYNTAX---->  01---- var_name.sort
#              02---- var_name.sort(reverse-false) #false=(a)lower,(d)=bigger


#              03----- var_name.sort(reverse=true)
             #True=,(d)=bigger to (a)lower


c=[100.43,45,77,99,00]
c.sort()
c
[0, 45, 77, 99, 100.43]


c.sort(reverse=False)
c
[0, 45, 77, 99, 100.43]

c.sort(reverse=True)
c
[100.43, 99, 77, 45, 0]



d=["apple","Apple","ball","Ball","cat","Cat"]
d.sort()
d
['Apple', 'Ball', 'Cat', 'apple', 'ball', 'cat']

ord(a)
Traceback (most recent call last):
  File "<pyshell#340>", line 1, in <module>
    ord(a)
TypeError: ord() expected string of length 1, but list found
ord("A")
65
ord("B")
66
ord("C")
67
ord("D")
68
ord("a")
97
ord("c")
99



x=["apple","apply"]
x.sort()
x
['apple', 'apply']
x=["christmas","apply"]
x.sort()
x
['apply', 'christmas']


#if both words are same then i
#here first come first serve is applide by default



z=["snapchat","instagram","walmart","sql","fb","a"]


z.sort(key=len)
z
['a', 'fb', 'sql', 'walmart', 'snapchat', 'instagram']
z.sort(key=len,reverse=False)
Z
Traceback (most recent call last):
  File "<pyshell#369>", line 1, in <module>
    Z
NameError: name 'Z' is not defined. Did you mean: 'z'?
z
['a', 'fb', 'sql', 'walmart', 'snapchat', 'instagram']
z.sort(key=len,reverse=True)
z
['instagram', 'snapchat', 'walmart', 'sql', 'fb', 'a']


>>> 
>>> 
>>> #syntax sort------  01--->v_n.sort(key=len,reverse=False)
>>> #                   02--->v_n.sort(key=len,reverse=True)
>>> 
>>> z.sort(reverse=False)
>>> z
['a', 'fb', 'instagram', 'snapchat', 'sql', 'walmart']
>>> z.sort(reverse=True)
>>> z
['walmart', 'sql', 'snapchat', 'instagram', 'fb', 'a']
>>> 
>>> 
>>> 
>>> a=[1,2,3,4,5]
>>> b=10,20,30,40,50]
SyntaxError: unmatched ']'
>>> b=[10,20,30,40,50]
>>> a+b
[1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
>>> 
>>> 
>>> #UNPACKING:---->
>>> 
...  
>>> 
>>> print(*a)
1 2 3 4 5
>>> print(*b)
10 20 30 40 50
>>> 
>>> x=[*a,*b]
>>> x
[1, 2, 3, 4, 5, 10, 20, 30, 40, 50]

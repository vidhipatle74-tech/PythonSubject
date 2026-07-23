Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
       #BITWISE OPERATOR:

#it will convert the given  integer number into the binary digits and perform bit bt bit operation

#integer is the only data type which suppoers bitwise operator

#THERE ARE THREE TYPES OF BITWISE OPERATOR :


#  (1) bitwise (AND)operator(&)
#  (2) bitwise (OR)operator(\)
#  (3) bitwise (XOR)operator(^)
#  (4) bitwise (NOT)operator(~)
#  (4) bitwise (LEFT SHIFT)operator(<<)
#  (6) bitwise (RIGHT SHIFT)operator(>>)



#  (1) bitwise (AND)operator(&):

# it will convert given integer numnber into binary digit and perform bit by bit (and) operation



#             TRUTH TABLE:

#           OPERAND 1    OPERAND 2       RESULT

#             0           0                  0
#             1           0                  0
#             0           1                  0
#             1           1                  1




19 & 13
1
24 & 17
16
54 & 32
32
47 & 37
37
24 & 19
16
16 & 8
0



##  (2) bitwise (OR)operator(\)


# it will convert the given integer number into binary digit  and perform bit by bit operation

#SYNTAX--->   op1 / op2

30 or 25
30
30|25
31
42|33
43
#SYNTAX-->     op1 | op2



#  (3) bitwise (XOR)operator(^)


#                         TRUTH TABLE
#             OP1               OP2               RESULT

#              1                 1                   0
#              0                 1                   1
#              1                 0                   1
#              1                 1                   0


# if both the operands are same  then o/p will be zero

38|33
39
38^33
7
29^19
14
44^22
58
53^39
18
14^7
9
39^30
57
24^17
9
21^20
1
29|19
31
44|22
62
53|39
55


#  (4) bitwise (NOT)operator(~)

# it will invert the result

   
  # SYNTAX:----> ~OPERAND1
  

#FORMULA--->  -(OP1+1)
  

~25
-26
~36
-37
~-37
36
~99
-100
~-72
71
~36
-37
#-(25=1)
#-(26)######




#  (4) bitwise (LEFT SHIFT)operator(<<)

14<<2
56
17<<3
136


#It will shift the position of binary  digits toward LHS

>>> #SYNTAX--->>> OP1 << N
>>> 
>>> #WHERE,
>>> #      "n" must be integer
>>> 
>>> #here the value is increse
>>> 
>>> 
>>> #  (6) bitwise (RIGHT SHIFT)operator(>>)
>>> 
>>> #It will shift the position of binary  digits toward RHS
>>> 
>>> 
>>>     #SYNTAX--->>> OP1 >> N
>>> 
>>> 18<<3
144
>>> 17>>3
2
>>> 18>>3
2
>>> 25>>3
3
>>> 257>>36
0
>>> #here the value is DECREASE
>>> 
>>> 
>>> 
>>> 

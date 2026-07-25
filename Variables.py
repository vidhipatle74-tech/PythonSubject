Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
            #VARIABLE:

# It is a container which is  used to store the data or the information is called variable.

      
   #SYNTAX: Variable_name =value

#It is a name given to a memory location which holds the actul data.
#A variable can holds objects of different types.
# all vaeiable should be in lowercase.
# we can seperate variable using underscore.


#RULES OF VARIABLSE:

#RULE(1:)
#RULE(1)--> We can use alphabet which will be in lowercase uppercase.
#example:-->
            xyz=123
            
SyntaxError: unexpected indent
           xyz='123'
           
SyntaxError: unexpected indent

#RULE(2):--> We can not start variable with number but, we can use it in between or end.

45ab=123
SyntaxError: invalid decimal literal
ab45=123
ab45
123

#RULE(3):-->We cannot use special character except underscore(_)

ca sh=123
SyntaxError: invalid syntax
ca_sh=123
ca_sh
123

#RULE(4):--> In the part of variables we cant use keywords

in=123
SyntaxError: invalid syntax

In=223
In
223

#RULE(5)--> In variables parts we can pass unlimited character , but according to PEP8 rule we can pass only 79 character.
#if we pass more than 79 or less than 79 ,then no error will be occured ,because its only rule

#PEP8:
      #it is a official python coadimg style guide.

# p --> python
# E --> enhancement
# P --> proposal
# 8 --> Version

# it provide rule and recommandations for writting python code.

>>> 
>>> #WHY??
>>> 
>>> #-->improve code readibility
>>> #-->makes code easier to debug and maintain.
>>> 
>>> 
>>> #CASES OF VARIABLES:
>>> 
>>> #(1) SNAKE CASE-->
>>> #                  --> Words are in lowercaes.
>>> #                  -->it is seperated by the special character called underscore(_)
>>> 
>>> #example:
>>> #         first_name
>>> 
>>> 
>>> #(2) CAMEL CASE-->
>>> #                 --> if we have two words where first word is in lowercaes .
>>> #                 --> after space first letter of second word is in upper case called camel case
>>> 
>>> #example:
>>> #        firstName
>>> 
>>> 
>>> #(3) PASCAL CASE-->
>>> #                  --> if whe have two words where first letter of first word is in uppercase and after the space                         first letter of second word is in uppercase thats callse pascal case.
>>> 
>>> #example:

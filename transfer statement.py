#---------------------------------------------------------------------------------------------------
#TRANSFER STATEMENTS
#---------------------------------------------------------------------------------------------------

#1.break:
    #---> break is a keyword it is used to stop the execution and come outside the loop

#example:--->
#wap to print the number until it meets double digit
'''
l=[1,2,7,9,4,3,10,11,8,2,3]
for i in l:
    if i>=10:
        break
    print(i,end=" ")
'''
#wap to terminate after it encounters 5 in the range(1-10)
'''
for i in range(1,11):
    if i==5:
        break
    print(i,end=" ")
'''

#wap to traverse through a string and stop the execution at specified character
#specified character is --->"y"
'''
s="hello guys you are working really hard super"
for i in s:
    if i=="y":
        break
    print(i,end=" ")
'''

#2.continue:
#---> continue will skip the current iteration and force the control to move to next iteration

#example:---->
#wap to print 1-10 and skip the iteration at 5
'''
for i in range(1,11):
    if i==5:
        continue
    print(i,end=" ")
'''



#wap to print only positive numbers
'''
l=[1,5,-2,-45,55,88,-100,-63]
for i in l:
    if i<0:
        continue
    print(i,end=" ")
'''


#wap to skip all the vowels in the given string
'''
s="good morning guys welcome to python session"
for i in s:
    if i in "aeiou":
        continue
    print(i,end=" ")
'''


#3.pass:
#---> It is used to perform no action on it and it helps in avoiding the errors

#pass also you can right---->...



example:------->
s="hey guys cool"
for i in s: #here it will show error if we run the code 
# IndentationError: expected an indented block after 'for' statement on line 594



s="hey guys cool"
for i in s:
    pass              #pass------>...




s="hey guys cool"
for i in s:
    ...
print(i)   #here always it will print last character
"""

#----------------------------------------------------------------------------------------------
#BREAK:
#------------------------------------------------------------------------------------------------
#       --> if you want to stop the execution immediately that time we use break keyword.
#      --> once your condition becomes false automatically it will move to next line.
#      --> once your condition becomes  true  automatically it will stops the execution immediately.
#      --> it is also known as tranverse statement
'''
a="Good Morning"
stop="d"

for i in a :
    if i==stop:
        break
    print(i)
'''
'''
#wap to print only number before double value.
d=[1,2,10,12,3,4,17]
for i in d:
    if i >=10:
        break
    ptint(i)
'''

#wap to print only negative values from the given list.
'''
s=[1,12,-3,90,-4,-5,900,-12]
for i in s:
    if i<0:
        print(i)
        break

'''
#----------------------------------------------------------------------------------------
#CONTINUE:
#-------------------------------------------------------------------------------------------
#        --> if the condition becomes true it will skip that number which are in condition.
#        --> it will skip the current iteration and move to next number.
#      --> it is also known as tranverse statement
'''
s="python class"
stop="n"

for i in s:
    if i==stop:
        break
    print(i,end=" ")  #o/p--> pytho

for i in s:
    if i==stop:
        continue
    print(i,end=" ")  #o/p--> pytho class  (n)->current iteration skip.
'''
#-------------------------------------------------------------------------------------------
#PASS:
#-------------------------------------------------------------------------------------------
#     --> if you want to avoid indentetion error you can use pass kayword
#     --> we can holds the case using pass keyword.
#     --> in the place of pass-->(...)
#     --> it is also known as tranverse statement
'''
k=[1,2,3,4,5,6,7]
for i in k:
    if i%2==0:
        pass
    print(i)
'''

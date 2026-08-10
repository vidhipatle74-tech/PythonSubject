
#NESTED FOR LOOP:

# outer for loop:-->outer formate it will execut for one time
# inner for loop:--> inner for loop it will ecexute completly

#outer for loop-->

      #syntax:    for outer in iterable:
      #           <-->statement

#inner for loop-->

      #syntax:    for inner in iterable:
      #           <-->statement

s=[[1,2,3],[4,5,6],[7,8,9]]
for i in s:
    print(i)
    for j in i:
        if j%2==0:
            print(j)





'''
#wap to print even length

e=[["good","bad","mad"],["sql"],["lovely","done","deal"]]

for i in e:
    for j in i:
        if len(e)==0:
            print(i)

'''

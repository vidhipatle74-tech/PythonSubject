#(1)
'''
rows=int(input("enter the rows:"))
columns=int(input("enter the columns:"))
for i in range(rows):
    for j in range(columns):
        if i%2==1 and j%2==1:
            print('',end=' ')
        else:
            print('*',end=' ')
    print()

#o/p-->
        enter the rows:7
        enter the columns:8
        * * * * * * * * 
        *  *  *  *  
        * * * * * * * * 
        *  *  *  *  
        * * * * * * * * 
        *  *  *  *  
        * * * * * * * * 
'''
#(2)

rows=int(input())

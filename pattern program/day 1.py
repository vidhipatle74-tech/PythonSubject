rows=int(input("enter the rows:"))
columns=int(input("enter the columns:"))
for i in range(rows):
    for j in range(columns):
        if i%2==1 and j%2==1:
            print('',end=' ')
        else:
            print('*',end=' ')
    print()

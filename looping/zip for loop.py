#ZIP FOR LOOP():
#               --> It is a inbuilt function.
#               --> the output will be in tuple form.
#               --> we have to pass same position of data.
#               --> it match position to position.

#SYNTAX-->     zip(iterable1,iterable2........)

#if length is matched data loss will be happens.
#iterable length should be equal.

#SYNTAX:---> LOOPING :--->
#                         for i in zip(iterable1,iterable2,.....)



#EXAMPLE-->

x=(10,20,30)
y=[1,2,3]

for i in zip(x,y):
    print(i)

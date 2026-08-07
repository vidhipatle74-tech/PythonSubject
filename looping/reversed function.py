
#REVERSED-->

#it is a inbuilt function.

#in reverse if we done operation directly it will show object address.

#in reversed to avoide object address data we have :

#  TWO WAYS-->

#             (1)Typecasting
#             (2)looping

#typecasting syntax:-->
#                      list(reversed(iterable))
#                      tuple(reversed(iterable))
#                      set(reversed(iterable))
#                      dict(reversed(iterable))
#                      string(reversed(iterable))
'''
s="hello"

print(set(reversed(s)))

#             output-->{'o', 'e', 'l', 'h'}

print(dict(reversed(s)))

#           output-->value error

print(tuple(reversed(s)))

#            output-->('o', 'l', 'l', 'e', 'h')

print(list(reversed(s)))

#            output-->['o', 'l', 'l', 'e', 'h']
'''
'''
d=[1,2,3,4,5]

for i in reversed(d):
    print(i)

    #output-->
              5
              4
              3
              2
              1

for i in range(-1,-len(d),-1):
    print(i)

    #output-->
              -1
              -2
              -3
              -4
'''
#wap to check how many words are present in the given string
a="hello world sentence"
'''
total=0
for i in a.split():
    total=total+1
print(total)
 '''   

#how to create a dict and print the character and its ascii value pair

s="hello world"

#wap to 

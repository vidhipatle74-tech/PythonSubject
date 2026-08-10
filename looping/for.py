#wap to remove duplicate elements in the given list.
'''
d=[1,2,3,4,5,6,1,2,3,4]
k=[]
for i in d:
    if i not in k:
        print(i)
'''
##1. WAP to extract only file names
l= ['forloop.txt', 'python.py', 'while.pdf', 'functions.pptx',
    'lambda.png', 'map.py', 'python.pdf', 'oops.py']
#output:-['forloop', 'python', 'while', 'functions', 'lambda', 'map', 'oops']

k=[]
for i in l:
    m=i.split(".")
    print(m)

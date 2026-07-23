Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#(6)--count()
#syntax: v_n.count()

#syntax: v_n.count('substracting', startindex, endindex+1)
# to check the single  character how many time they repeated
y='Good Morning'
y.count(Good)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    y.count(Good)
NameError: name 'Good' is not defined
y.count("Good)
        
SyntaxError: unterminated string literal (detected at line 1)
y.count("Good")
        
1
y.count("o")
        
3
y.count("p")
        
0
y.count("o")
        
3
y.count("o",0,3)
        
2
y.count("Morning")
        
1
len(y)
        
12







r="Python class and Morning session"
        
y.count("o")
        
3


y.count("Python class ")
        
0
r.count("Python class")
        
1

>>> 
>>> r=("0", 10,32")
...    
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> r=("0",10,32)
...    
>>> r.count("s",10,32)
...    
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    r.count("s",10,32)
TypeError: tuple.count() takes exactly one argument (3 given)
>>> 
>>> 
>>> r.count("s",10,32)
...    
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    r.count("s",10,32)
TypeError: tuple.count() takes exactly one argument (3 given)
>>> r.count("s",0,32)
...    
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    r.count("s",0,32)
TypeError: tuple.count() takes exactly one argument (3 given)
>>> 
>>> 
>>> r
...    
('0', 10, 32)
>>> r="Python class and Morning session"
...    

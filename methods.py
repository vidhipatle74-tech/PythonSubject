Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #REPLACE()
>>> 
>>> #SYNTAX------> v_n.replace('oldcharacter','newcharacter',count)--count is optional
>>> 
>>> z="hello"
>>> z.replace("l","o")
'heooo'
>>> 
>>> #we cant rplace second occurance of the character only we can first
>>> 
>>> z.replace("hello","python")
'python'
>>> 
>>> z.replace("Hello","python")
'hello'
>>> #we can not replace original word
>>> 
>>> 
>>> k="Good Morning"
>>> k.replace("o",8,)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    k.replace("o",8,)
TypeError: replace() argument 2 must be str, not int
>>> KeyboardInterrupt
>>> k.replace("o",8)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    k.replace("o",8)
TypeError: replace() argument 2 must be str, not int
>>> k.replace("o","8")
'G88d M8rning'
>>> k.replace("o","8",2)
'G88d Morning'

Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=2
print(bool(a))
True

a=10
type(a)
<class 'int'>

a='missing'
int(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'missing'
float(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    float(a)
ValueError: could not convert string to float: 'missing'
complex(a)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    complex(a)
ValueError: complex() arg is a malformed string
bool(a)
True
str(a)
'missing'
>>> list(a)
['m', 'i', 's', 's', 'i', 'n', 'g']
>>> tuple(a)
('m', 'i', 's', 's', 'i', 'n', 'g')
>>> set(a)
{'m', 'n', 's', 'g', 'i'}
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> a='123'
>>> int(a)
123
>>> float(a)
123.0
>>> complex(a)
(123+0j)
>>> bool(a)
True
>>> str(a)
'123'
>>> list(a)
['1', '2', '3']
>>> tuple(a)
('1', '2', '3')
>>> set(a)
{'3', '1', '2'}
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required

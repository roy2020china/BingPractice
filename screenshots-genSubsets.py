Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 20:42:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets.py =============
>>> L=['a','b','c','d']
>>> genSubsets(L)
[[], ['a'], [['a', 'b']], [['a', 'c']], [['a', 'd']], [['a', 'b', 'c']], [['a', 'b', 'd']], [['a', 'b', 'c', 'd']], ['b'], [['b', 'c']], [['b', 'd']], [['b', 'c', 'd']], ['c'], [['c', 'd']], ['d']]
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets.py =============
>>> L=['a','b','c','d']
>>> genSubsets(L)
[[], ['a'], ['a', 'b'], ['a', 'c'], ['a', 'd'], ['a', 'b', 'c'], ['a', 'b', 'd'], ['a', 'b', 'c', 'd'], ['b'], ['b', 'c'], ['b', 'd'], ['b', 'c', 'd'], ['c'], ['c', 'd'], ['d']]
>>> 
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 20:42:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets2.py =============
>>> l['A', 'B', 'C','D']
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    l['A', 'B', 'C','D']
NameError: name 'l' is not defined
>>> L = ['A', 'B', 'C','D']
>>> res4 = genSubsets4(L)
L =  ['A', 'B', 'C', 'D'] BEFORE recursion
L =  ['A', 'B', 'C'] BEFORE recursion
L =  ['A', 'B', 'C', 'D'] AFTER recursion
extra =  ['D']
small in smaller =  l  in  length of L = 3 when 'return' executed
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    res4 = genSubsets4(L)
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 111, in genSubsets4
    new.append(small + extra)
TypeError: can only concatenate str (not "list") to str
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets2.py =============
>>> L = ['A', 'B', 'C','D']
>>> res4 = genSubsets4(L)
L =  ['A', 'B', 'C', 'D'] BEFORE recursion
L =  ['A', 'B', 'C'] BEFORE recursion
L =  ['A', 'B', 'C', 'D'] AFTER recursion
extra =  ['D']
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    res4 = genSubsets4(L)
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 110, in genSubsets4
    for small in smaller:
TypeError: 'int' object is not iterable
>>> type(L)
<class 'list'>
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets2.py =============
>>> L = ['A', 'B', 'C','D']
>>> res4 = genSubsets4(L)
L =  ['A', 'B', 'C', 'D'] BEFORE recursion
L =  ['A', 'B', 'C'] BEFORE recursion
L =  ['A', 'B', 'C', 'D'] AFTER recursion
extra =  ['D']
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    res4 = genSubsets4(L)
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 110, in genSubsets4
    for small in smaller:
TypeError: 'int' object is not iterable
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets2.py =============
>>> L = ['A', 'B', 'C','D']
>>> res4 = genSubsets4(L)
L =  ['A', 'B', 'C', 'D'] BEFORE recursion
L =  ['A', 'B', 'C'] BEFORE recursion
L =  ['A', 'B', 'C', 'D'] AFTER recursion
extra =  ['D']
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    res4 = genSubsets4(L)
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 110, in genSubsets4
    print('type of small is ', type(small), '\n', 'type of smaller is ', type(smaller))
UnboundLocalError: local variable 'small' referenced before assignment
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets2.py =============
>>> L = ['A', 'B', 'C','D']
>>> res4 = genSubsets4(L)
L =  ['A', 'B', 'C', 'D'] BEFORE recursion
L =  ['A', 'B', 'C'] BEFORE recursion
L =  ['A', 'B', 'C', 'D'] AFTER recursion
extra =  ['D']
type of smaller is  <class 'int'>
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    res4 = genSubsets4(L)
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 113, in genSubsets4
    for small in smaller:
TypeError: 'int' object is not iterable
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets2.py =============
>>> L = ['A', 'B', 'C','D']
>>> res4 = genSubsets4(L)
L =  ['A', 'B', 'C', 'D'] BEFORE recursion
L =  ['A', 'B', 'C'] BEFORE recursion
L =  ['A', 'B'] BEFORE recursion
L =  ['A', 'B', 'C'] AFTER recursion
extra =  ['C']
type of smaller is  <class 'int'>
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    res4 = genSubsets4(L)
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 102, in genSubsets4
    smaller = genSubsets4(L[:-1])
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 113, in genSubsets4
    for small in smaller:
TypeError: 'int' object is not iterable
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets2.py =============
>>> res4 = genSubsets4(L)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    res4 = genSubsets4(L)
NameError: name 'L' is not defined
>>> L = ['A', 'B', 'C','D']
>>> res4 = genSubsets4(L)
L =  ['A', 'B', 'C', 'D'] BEFORE recursion
L =  ['A', 'B', 'C'] BEFORE recursion
L =  ['A', 'B'] BEFORE recursion
L =  ['A', 'B', 'C'] AFTER recursion
extra =  ['C']
type of smaller is  <class 'list'>
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    res4 = genSubsets4(L)
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 102, in genSubsets4
    smaller = genSubsets4(L[:-1])
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 119, in genSubsets4
    print('small + extra = ', small + extra)
UnboundLocalError: local variable 'small' referenced before assignment
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets2.py =============
>>> L = ['A', 'B', 'C','D']
>>> res4 = genSubsets4(L)
L =  ['A', 'B', 'C', 'D'] BEFORE recursion
L =  ['A', 'B', 'C'] BEFORE recursion
L =  ['A', 'B'] BEFORE recursion
L =  ['A', 'B', 'C'] AFTER recursion
extra =  ['C']
type of smaller is  <class 'list'>
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    res4 = genSubsets4(L)
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 102, in genSubsets4
    smaller = genSubsets4(L[:-1])
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 112, in genSubsets4
    print('small = ', small)
UnboundLocalError: local variable 'small' referenced before assignment
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets2.py =============
>>> L = ['A', 'B', 'C','D']
>>> res4 = genSubsets4(L)
L =  ['A', 'B', 'C', 'D'] BEFORE recursion
L =  ['A', 'B', 'C'] BEFORE recursion
L =  ['A', 'B'] BEFORE recursion
L =  ['A', 'B', 'C'] AFTER recursion
extra =  ['C']
type of smaller is  <class 'list'>
smaller =  []
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    res4 = genSubsets4(L)
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 102, in genSubsets4
    smaller = genSubsets4(L[:-1])
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 119, in genSubsets4
    print('small + extra = ', small + extra)
UnboundLocalError: local variable 'small' referenced before assignment
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets2.py =============
>>> L = ['A', 'B', 'C','D']
>>> res4 = genSubsets4(L)
L =  ['A', 'B', 'C', 'D'] BEFORE recursion
L =  ['A', 'B', 'C'] BEFORE recursion
L =  ['A', 'B'] BEFORE recursion
L =  ['A', 'B', 'C'] AFTER recursion
extra =  ['C']
type of smaller is  <class 'list'>
smaller =  [[]]
new =  [['C']]
small + extra =  ['C']
END OF genSubsets444444444444444444
L =  ['A', 'B', 'C', 'D'] AFTER recursion
extra =  ['D']
type of smaller is  <class 'NoneType'>
smaller =  None
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    res4 = genSubsets4(L)
  File "/Users/ABC/Temp/BingPython/genSubsets2.py", line 113, in genSubsets4
    for small in smaller:
TypeError: 'NoneType' object is not iterable
>>> x = [] + [c]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    x = [] + [c]
NameError: name 'c' is not defined
>>> x = [] + ['c']
>>> x
['c']
>>> x = [] + [['c']]
>>> x
[['c']]
>>> x = [[]] + [['c']]
>>> x
[[], ['c']]
>>> 
============= RESTART: /Users/ABC/Temp/BingPython/genSubsets2.py =============
>>> L = ['A', 'B', 'C','D']
>>> res4 = genSubsets4(L)
L =  ['A', 'B', 'C', 'D'] BEFORE recursion
L =  ['A', 'B', 'C'] BEFORE recursion
L =  ['A', 'B'] BEFORE recursion
L =  ['A', 'B', 'C'] AFTER recursion
extra =  ['C']
type of smaller is  <class 'list'>
smaller =  [[]]
new =  [['C']]
small + extra =  ['C']
END OF genSubsets444444444444444444
L =  ['A', 'B', 'C', 'D'] AFTER recursion
extra =  ['D']
type of smaller is  <class 'list'>
smaller =  [['C']]
new =  [['C', 'D']]
small + extra =  ['C', 'D']
END OF genSubsets444444444444444444
>>> rest4
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    rest4
NameError: name 'rest4' is not defined
>>> res4
[['C', 'D']]
>>> 

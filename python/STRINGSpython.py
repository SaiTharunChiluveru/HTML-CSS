Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="hello"
>>> s
'hello'
>>> s2="""this is line 1
this is linr 2
this is line 3"""
>>> s2
'this is line 1\nthis is linr 2\nthis is line 3'
>>> s[0]
'h'
>>> s2[0]
't'
>>> s2[1]
'h'
>>> s2[::-1]
'3 enil si siht\n2 rnil si siht\n1 enil si siht'
>>> s2[-1]
'3'
>>> s2[-5:-1]
'ine '
>>> "hello wrols".capitalize()
'Hello wrols'
>>> # captilize makes first letter capital
>>> "hello world".upper()
'HELLO WORLD'
>>> #upper() will make everything captal
>>> s[:-1]
'hell'
>>> a="j,k,l"
>>> a
'j,k,l'
>>> a2.count(t)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a2.count(t)
NameError: name 'a2' is not defined
>>> a2.count('t')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a2.count('t')
NameError: name 'a2' is not defined
>>> s2.count(t)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s2.count(t)
NameError: name 't' is not defined
>>> s2.count('t')
3
>>> for i in s:
	print(s)

	
hello
hello
hello
hello
hello
>>> s2.isupper()
False
>>> "Sub".isupper()
False
>>> "Varsh".isdigit()
False
>>> s.index('t')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s.index('t')
ValueError: substring not found
>>> s.index("this")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s.index("this")
ValueError: substring not found
>>> s2.index("thsi")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s2.index("thsi")
ValueError: substring not found
>>> s2.index("this")
0
>>> s.index('h')
0
>>> a.index(h)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a.index(h)
NameError: name 'h' is not defined
>>> tup=("hn","hj","kl")
>>> for i in tup
SyntaxError: invalid syntax
>>> for i in tup:
	k=k+tup[i]

	
Traceback (most recent call last):
  File "<pyshell#40>", line 2, in <module>
    k=k+tup[i]
NameError: name 'k' is not defined
>>> k=str
>>> k=str()
>>> for i in tup:
	k=k+tup[i]

	
Traceback (most recent call last):
  File "<pyshell#45>", line 2, in <module>
    k=k+tup[i]
TypeError: tuple indices must be integers or slices, not str
>>> for i in tup:
	k=k+i
    print(k)
    
SyntaxError: unindent does not match any outer indentation level
>>> 
KeyboardInterrupt
>>> for i in tup:
	k=k+i

	
>>> print(k)
hnhjkl
>>> tup=(1,2,"hi",4,'g',"world")
>>> for i in tup:
	k=k+i

	
Traceback (most recent call last):
  File "<pyshell#54>", line 2, in <module>
    k=k+i
TypeError: can only concatenate str (not "int") to str
>>> for i in tup:
	k=k+str(i)

	
>>> print(k)
hnhjkl12hi4gworld
>>> # strings are not hashable. they canaot be modifies directly.. we use replace() methood.
>>> k.replace("world","WORLD")
'hnhjkl12hi4gWORLD'
>>> k
'hnhjkl12hi4gworld'
>>> #strip() removes spaces from left and right.. lstrip(),rstrip()
>>> "  HELLO  ".strip()
'HELLO'
>>> "  HELLO  ".lstrip()
'HELLO  '
>>> #split() method separates the given str into parts,taking space as delimeter..
>>> "HELLO MAMA HOW ARE YOU".split()
['HELLO', 'MAMA', 'HOW', 'ARE', 'YOU']
>>> #split(',')  specifying delimeter
>>> "HELL,OO,WOR,LD".split(',')
['HELL', 'OO', 'WOR', 'LD']
>>> a5=['HELL', 'OO', 'WOR', 'LD']
>>> "".join(a)
'j,k,l'
>>> "".join(a5)
'HELLOOWORLD'
>>> 
KeyboardInterrupt
>>> " ".join(a5)
'HELL OO WOR LD'
>>> 
=============================================== RESTART: C:/Users/sunny/OneDrive/Desktop/python/noofdistinctcharinstr.py ==============================================
Traceback (most recent call last):
  File "C:/Users/sunny/OneDrive/Desktop/python/noofdistinctcharinstr.py", line 6, in <module>
    co=di[i]
KeyError: 'H'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/sunny/OneDrive/Desktop/python/noofdistinctcharinstr.py", line 8, in <module>
    co=co+1
NameError: name 'co' is not defined
>>> 
=============================================== RESTART: C:/Users/sunny/OneDrive/Desktop/python/noofdistinctcharinstr.py ==============================================
Traceback (most recent call last):
  File "C:/Users/sunny/OneDrive/Desktop/python/noofdistinctcharinstr.py", line 10, in <module>
    di.update({i:x})
NameError: name 'x' is not defined
>>> 
=============================================== RESTART: C:/Users/sunny/OneDrive/Desktop/python/noofdistinctcharinstr.py ==============================================
{'H': 2, 'E': 1, 'L': 2, 'O': 1, ' ': 10, 'm': 5, 'a': 4, 'y': 3, 'n': 2, 'e': 3, 'i': 2, 's': 1, 'T': 1, 'A': 2, 'R': 1, 'U': 1, 'N': 1, 'h': 1, 'o': 2, 'w': 1, 'r': 1, 'u': 1, 'I': 1, 'f': 1}
>>> 
=============================================== RESTART: C:/Users/sunny/OneDrive/Desktop/python/noofdistinctcharinstr.py ==============================================
{'H': 2, 'E': 1, 'L': 2, 'O': 1, ' ': 10, 'm': 5, 'a': 4, 'y': 3, 'n': 2, 'e': 3, 'i': 2, 's': 1, 'T': 1, 'A': 2, 'R': 1, 'U': 1, 'N': 1, 'h': 1, 'o': 2, 'w': 1, 'r': 1, 'u': 1, 'I': 1, 'f': 1}
>>> 

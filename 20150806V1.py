Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def odd():
	print 'step 1'
	yield 1
	print 'step 2'
	yield 3
	print 'step 3'
	yield 5

	
>>> o = odd()
>>> o.next()
step 1
1
>>> o.next()
step 2
3
>>> o.next()
step 3
5
>>> o.next()

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    o.next()
StopIteration
>>> def fib(max):
	n, a, b = 0, 0, 1
	while n <max:
		yield b
		a, b = b, a+b
		n = n+1

		
>>> fib(6)
<generator object fib at 0x0210FEB8>
>>> for n in fib(6)
SyntaxError: invalid syntax
>>> for n in fib(6):
	print n

	
1
1
2
3
5
8
>>> abs(-10)
10
>>> abs
<built-in function abs>
>>> x = abs(-10)
>>> x
10
>>> y == abs(-10)

Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    y == abs(-10)
NameError: name 'y' is not defined
>>> y ==0

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    y ==0
NameError: name 'y' is not defined
>>> y = 0
>>> y== 0
True
>>> a = abs()

Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a = abs()
TypeError: abs() takes exactly one argument (0 given)
>>> a = abs
>>> a
<built-in function abs>
>>> a(-10)
10
>>> abs = 10
>>> ans

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    ans
NameError: name 'ans' is not defined
>>> abs
10
>>> abs(-10)

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    abs(-10)
TypeError: 'int' object is not callable
>>> abs = abs()

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    abs = abs()
TypeError: 'int' object is not callable
>>> def add(x, y, f):
	return f(x) + f(y)

>>> f

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    f
NameError: name 'f' is not defined
>>> f = abs
>>> f
10
>>> 

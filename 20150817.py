Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> type(123)
<class 'int'>
>>> typr('str')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    typr('str')
NameError: name 'typr' is not defined
>>> type('str')
<class 'str'>
>>> type(None)
<class 'NoneType'>
>>> type(abs)
<class 'builtin_function_or_method'>
>>> type(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
>>> type(123) == type(456)
True
>>> type('abc') == type('123')
True
>>> type('abc') == type(123)
False
>>> import types
>>> type('abc') == types.StringType
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    type('abc') == types.StringType
AttributeError: 'module' object has no attribute 'StringType'
>>> type('abc')
<class 'str'>
>>> type('abc') == types.StringType
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    type('abc') == types.StringType
AttributeError: 'module' object has no attribute 'StringType'
>>> import types
>>> type('abc') == types.StringType
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    type('abc') == types.StringType
AttributeError: 'module' object has no attribute 'StringType'
>>> types
<module 'types' from 'C:\\Python34\\lib\\types.py'>
>>> type(u'abs')
<class 'str'>
>>> type([])
<class 'list'>
>>> type(str)
<class 'type'>
>>> type(str) == types.TypeType
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    type(str) == types.TypeType
AttributeError: 'module' object has no attribute 'TypeType'
>>> type(str) == types.Type
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    type(str) == types.Type
AttributeError: 'module' object has no attribute 'Type'
>>> type(str) ==types.type
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    type(str) ==types.type
AttributeError: 'module' object has no attribute 'type'
>>> import types
>>> types
<module 'types' from 'C:\\Python34\\lib\\types.py'>
>>> type('abs') == types.str
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    type('abs') == types.str
AttributeError: 'module' object has no attribute 'str'
>>> types.FunctionType
<class 'function'>
>>> 
>>> types.str
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    types.str
AttributeError: 'module' object has no attribute 'str'
>>> str
<class 'str'>
>>> types('abx') == str
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    types('abx') == str
TypeError: 'module' object is not callable
>>> a = Animal()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a = Animal()
NameError: name 'Animal' is not defined
>>> class Animal():
	pass

>>> 
>>> a = Animal()
>>> calss Dog(Animal)
SyntaxError: invalid syntax
>>> class Dog(Animal):
	pass

>>> class Husky(Dog):
	pass

>>> d = Dog()
>>> h = Husky()
>>> isinstance(h, Husky)
True
>>> isinstance(h,Dog)
True
>>> isinstance(h,Animal)
True
>>> isinstance(d,Dog) and isinstance(d,Animal)
True
>>> 
>>> isinstance(d,Husky)
False
>>> isinstance('a',str)
True
>>> isinstance('a',unicode)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    isinstance('a',unicode)
NameError: name 'unicode' is not defined
>>> isinstance('a',(str,int))
True
>>> isinstance('a',basestring)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    isinstance('a',basestring)
NameError: name 'basestring' is not defined
>>> dir('ABC')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> len('ABC')
3
>>> 'ABV'.__len__()
3
>>> class MyObject(object):
	def __len__(self):
		return 100

	
>>> obj = MyObject()
>>> len(obj)
100
>>> 'ABC'.lower()
'abc'
>>> class MyObject(object):
	def __init__(self)"
	
SyntaxError: EOL while scanning string literal
>>> class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * slef.x

	
>>> obj = MyObject()
>>> hasattr(obj, 'x')
True
>>> obj.x
9
>>> hassattr(obj,'y')
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    hassattr(obj,'y')
NameError: name 'hassattr' is not defined
>>> hasattr(obj,'y')
False
>>> setattr(obj,'y',19)
>>> hasattr(obj,'y')
True
>>> getattr(obj,'y')
19
>>> obj.y
19
>>> getattr(obj,'z')
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    getattr(obj,'z')
AttributeError: 'MyObject' object has no attribute 'z'
>>> getattr(obj,'z',404)
404
>>> hasattr(obj,'power')
True
>>> getattr(obj,'power')
<bound method MyObject.power of <__main__.MyObject object at 0x0237BB30>>
>>> fn = getattr(obj,'power')
>>> fn
<bound method MyObject.power of <__main__.MyObject object at 0x0237BB30>>
>>> fn()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    fn()
  File "<pyshell#73>", line 5, in power
    return self.x * slef.x
NameError: name 'slef' is not defined
>>> obj.power()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    obj.power()
  File "<pyshell#73>", line 5, in power
    return self.x * slef.x
NameError: name 'slef' is not defined
>>> setattr(obj,'power',81)
>>> fn()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    fn()
  File "<pyshell#73>", line 5, in power
    return self.x * slef.x
NameError: name 'slef' is not defined
>>> fn
<bound method MyObject.power of <__main__.MyObject object at 0x0237BB30>>
>>> getattr(obj ,'power')
81
>>> fn()
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    fn()
  File "<pyshell#73>", line 5, in power
    return self.x * slef.x
NameError: name 'slef' is not defined
>>> fn
<bound method MyObject.power of <__main__.MyObject object at 0x0237BB30>>
>>> fn = getattr(obj,'power')
>>> fn()
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    fn()
TypeError: 'int' object is not callable
>>> fn
81
>>> obj.power()
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    obj.power()
TypeError: 'int' object is not callable
>>> class Student(object):
	pass

>>> s = Student()
>>> s.name = 'Michael'
>>> print(s.name)
Michael
>>> def set_age(self,age):
	self.age = age

	
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s, Student)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    s.set_age = MethodType(set_age, s, Student)
TypeError: method expected 2 arguments, got 3
>>> s.set_age(25)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    s.set_age(25)
AttributeError: 'Student' object has no attribute 'set_age'
>>> def set_age(self, age):
	self.age = age

	
>>> from types import MethodType
>>> s.set_age = MethodType(set_age, s, Student)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    s.set_age = MethodType(set_age, s, Student)
TypeError: method expected 2 arguments, got 3
>>> MethodType
<class 'method'>
>>> import math
>>> math.sqrt(2)
1.4142135623730951
>>> def quadratic(a,b,c):
	if a == 0
	
SyntaxError: invalid syntax
>>> def quadratic(a,b,c):
	x1 == 1
	x2 == 1
	if a == 0:
		x1 = - c/b
		x2 = x1
	else :
		x1 = (b+ math.sqrt(b*b - 4*a*c))/(2*a)
		x2 = (b- math.sqrt(b*b - 4*a*c))/(2*a)
	print(x1,x2)
	return x1,x2

>>> quadratic(2,3,1)
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    quadratic(2,3,1)
  File "<pyshell#133>", line 2, in quadratic
    x1 == 1
UnboundLocalError: local variable 'x1' referenced before assignment
>>> def quadratic(a,b,c):
	if a == 0:
		x1 = - c/b
		x2 = x1
	else :
		x1 = (b+ math.sqrt(b*b - 4*a*c))/(2*a)
		x2 = (b- math.sqrt(b*b - 4*a*c))/(2*a)
	print(x1,x2)
	return x1,x2

>>> quadratic(2,3,1)
1.0 0.5
(1.0, 0.5)
>>> quadratic(1,3,-4)
4.0 -1.0
(4.0, -1.0)
>>> def quadratic(a,b,c):
	if a == 0:
		x1 = - c/b
		x2 = x1
	else :
		x1 = -(b+ math.sqrt(b*b - 4*a*c))/(2*a)
		x2 = -(b- math.sqrt(b*b - 4*a*c))/(2*a)
	print(x1,x2)
	return x1,x2

>>> quadratic(2,3,1)
-1.0 -0.5
(-1.0, -0.5)
>>> quadratic(1,3,-4)
-4.0 1.0
(-4.0, 1.0)
>>> def power(x):
	return x *x

>>> power(5)
25
>>> power(15)
225
>>> def power(x,n = 2):
	s =1
	while n >0
	
SyntaxError: invalid syntax
>>> def power(x,n=2):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	returm s
	
SyntaxError: invalid syntax
>>> def power(x,n=2):
	s = 1
	while n>0:
		n = n-1
		s = s*x
	return s

>>> power(5)
25
>>> power(5,3)
125
>>> def enroll(name,gender)
SyntaxError: invalid syntax
>>> def enroll(name,gender):
	print ('name:',name)
	print ('gender:',gender)

	
>>> enroll('Sarah','F')
name: Sarah
gender: F
>>> def enroll(name,gender,age=6,city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)

	
>>> enroll('Sarah','F')
name: Sarah
gender: F
age: 6
city: Beijing
>>> enroll('Adam','M',city='Tianjing')
name: Adam
gender: M
age: 6
city: Tianjing
>>> def add_end(L=[])
SyntaxError: invalid syntax
>>> def add_end(L=[]):
	L.append('END')
	return L

>>> add_end([1,2,3])
[1, 2, 3, 'END']
>>> add_end()
['END']
>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
>>> def add_end(L=[]):
	if  L is None:
		L[]
		
SyntaxError: invalid syntax
>>> def add_end(L):
	if L is None:
		L = []
	L.append('End')
	return L

>>> add_end()
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    add_end()
TypeError: add_end() missing 1 required positional argument: 'L'
>>> def add_end(L=[]):
	if L is None:
		L = []
	L.append('End')
	return L

>>> add_end()
['End']
>>> add_end()
['End', 'End']
>>> def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

>>> add_end()
['END']
>>> add_end()
['END']
>>> def clac(numbers):
	sum = 0
	for n in numbers:
		sum = n*n+sum
	return sum

>>> calc([1,2,3])
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    calc([1,2,3])
NameError: name 'calc' is not defined
>>> clac([1,2,3])
14
>>> clac((1,3,5,7))
84
>>> clac(1,2,3,4)
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    clac(1,2,3,4)
TypeError: clac() takes 1 positional argument but 4 were given
>>> def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum+n*n
	return sum

>>> calc(1,2,3,3)
23
>>> calc()
0
>>> def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

	
>>> person('Michael',30)
name: Michael age: 30 other: {}
>>> person('Sam',29,city='beijing',gender = 'M')
name: Sam age: 29 other: {'city': 'beijing', 'gender': 'M'}
>>> extra = {'city':'Beijing','job':'Engineer'}
>>> person('Jack',24,**extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
>>> def person (name,age,**kw):
	if 'city'in kw:
		pass
	if 'job' in kw:
		pass
	print('name:',name,'age:',age,'other:',kw)

	
>>> person('Jack',24,addr = 'Changyang',zipcode='100045')
name: Jack age: 24 other: {'zipcode': '100045', 'addr': 'Changyang'}
>>> def person(name,age,*,city,job):
	print(name,age,city,job)

	
>>> person('Jack',25,city='BJ',job='Engineer')
Jack 25 BJ Engineer
>>> person('Jack',25,'BJ','Engineer')
Traceback (most recent call last):
  File "<pyshell#249>", line 1, in <module>
    person('Jack',25,'BJ','Engineer')
TypeError: person() takes 2 positional arguments but 4 were given
>>> def f1(a,b,c=0,*args,**kw):
	print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

	
>>> def f2(a,b,c=0,*,d,**kw):
	print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

	
>>> f1(1,2)
a= 1 b= 2 c= 0 args= () kw= {}
>>> f1(1,2,3)
a= 1 b= 2 c= 3 args= () kw= {}
>>> f1(1,2,3,4,5,6)
a= 1 b= 2 c= 3 args= (4, 5, 6) kw= {}
>>> f1(1,2,kw=5)
a= 1 b= 2 c= 0 args= () kw= {'kw': 5}
>>> f1(1,2,x=4)
a= 1 b= 2 c= 0 args= () kw= {'x': 4}
>>> f2(1,2,3,4,5,)
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    f2(1,2,3,4,5,)
TypeError: f2() takes from 2 to 3 positional arguments but 5 were given
>>> f2(1,2,3,4,5,6,7)
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    f2(1,2,3,4,5,6,7)
TypeError: f2() takes from 2 to 3 positional arguments but 7 were given
>>> f2(1,2,3)
Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    f2(1,2,3)
TypeError: f2() missing 1 required keyword-only argument: 'd'
>>> f2(1,2,d=3)
a= 1 b= 2 c= 0 d= 3 kw= {}
>>> f2(1,2,3,4,5,d=10,ext=None)
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    f2(1,2,3,4,5,d=10,ext=None)
TypeError: f2() takes from 2 to 3 positional arguments but 5 positional arguments (and 1 keyword-only argument) were given
>>> f2(1,2,3,d=10,ext=None)
a= 1 b= 2 c= 3 d= 10 kw= {'ext': None}
>>> def f3(a,b,c=0,*args,**ab):
	print('a=',a,'b=',b,'c=',c,'args=',args,'ab=',ab)

	
>>> f3(1,2,erere=999)
a= 1 b= 2 c= 0 args= () ab= {'erere': 999}
>>> args = (1,2,3,4)
>>> kw = {'d':99,'x':'#'}
>>> f1(*args,**kw)
a= 1 b= 2 c= 3 args= (4,) kw= {'d': 99, 'x': '#'}
>>> args = (1,2,3)
>>> f2(*agrs,**kw)
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    f2(*agrs,**kw)
NameError: name 'agrs' is not defined
>>> args = (1,2,3)
>>> kw = {'d':99,'x':'#'}
>>> f2(*args,**kw)
a= 1 b= 2 c= 3 d= 99 kw= {'x': '#'}
>>> def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

>>> fact(1)
1
>>> fact(5)
120
>>> fact(100)
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> fact(1000)
Traceback (most recent call last):
  File "<pyshell#286>", line 1, in <module>
    fact(1000)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 4, in fact
    return n * fact(n-1)
  File "<pyshell#282>", line 2, in fact
    if n == 1:
RuntimeError: maximum recursion depth exceeded in comparison
>>> def fact(n):
	return fact_iter(n,1)

>>> def fact_iter(num,pro):
	if num == 1:
		return pro
	return fact_iter(num - 1 ,num *pro)

>>>  def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)
SyntaxError: unexpected indent
>>> def fact(n):
	return fact_iter(n,1)

>>> fact(100000)
Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    fact(100000)
  File "<pyshell#297>", line 2, in fact
    return fact_iter(n,1)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#294>", line 2, in fact_iter
    if num == 1:
RuntimeError: maximum recursion depth exceeded in comparison
>>> def fact(n):
	return fact_iter(n,1)

>>> def fact_iter(num,pro):
	if num == 1:
		return pro
	return fact_iter(num - 1 ,num *pro)

>>>  def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)
SyntaxError: unexpected indent
>>> def fact(n):
	return fact_iter(n,1)
SyntaxError: invalid syntax
>>> def fact(n):
	return fact_iter(n,1)

>>> def fact_iter(num,pro):
	if num == 1:
		return pro
	return fact_iter(num - 1 ,num *pro)

>>> fact(10)
3628800
>>> fact(1000)
Traceback (most recent call last):
  File "<pyshell#305>", line 1, in <module>
    fact(1000)
  File "<pyshell#301>", line 2, in fact
    return fact_iter(n,1)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#303>", line 2, in fact_iter
    if num == 1:
RuntimeError: maximum recursion depth exceeded in comparison
>>> def fact_iter(num,pro):
	if num == 1:
		return pro
	return fact_iter(num - 1 ,num *pro)

>>> fact(5)
120
>>> fact(1000)
Traceback (most recent call last):
  File "<pyshell#309>", line 1, in <module>
    fact(1000)
  File "<pyshell#301>", line 2, in fact
    return fact_iter(n,1)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 4, in fact_iter
    return fact_iter(num - 1 ,num *pro)
  File "<pyshell#307>", line 2, in fact_iter
    if num == 1:
RuntimeError: maximum recursion depth exceeded in comparison
>>> 

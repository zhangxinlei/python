Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Animal(object):
	pass

>>> class Dog(object):
	pass

>>> class Dog(Animal):
	pass

>>> class Husky(Dog):
	pass

>>> a = Animal()
>>> d = Dog()
>>> h = Husky()
>>> isinstance(h,Husky)
True
>>> isinstance(h,Dog)
True
>>> isinstance(h,Animal)
True
>>> isinstance(d,Dog) and isinstance(d,Animal)
True
>>> isinstance(d,Husky)
False
>>> isinstance('a',str)
True
>>> print('使用dir()')
使用dir()
>>> ============================
SyntaxError: invalid syntax
>>> #================
>>> dir('ABC')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> len('ABC')
3
>>> 'ABC'.__len__()
3
>>> class MyObject(object):
	def __len__(self):
		return 100

	
>>> obj = MyObject()
>>> len(obj)
100
>>> 'ABC' = MyObject()
SyntaxError: can't assign to literal
>>> hasattr(obj,'x') #有属性x么？
False
>>> obj.x
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    obj.x
AttributeError: 'MyObject' object has no attribute 'x'
>>> dir(MyObject)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> class MyObject

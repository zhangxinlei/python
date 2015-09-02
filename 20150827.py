#Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
#Type "copyright", "credits" or "license()" for more information.
>>> import functools
>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func
	print('end call')
	return wrapper

>>> @log
def now():
	print('20150827')

	
end call
>>> now()
call now():
<function now at 0x023746F0>
>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func
		print('end call')
	return wrapper

>>> @log
def now():
	print('20150827')

	
>>> now()
call now():
<function now at 0x023AC810>
>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
		print('end call')
	return wrapper

>>> @log
def now():
	print('20150827')

	
>>> now()
call now():
20150827
>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	print('end call')
	return wrapper

>>> @log
def now():
	print('20150827')

	
end call
>>> now()
call now():
20150827
>>> def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s  %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

>>> def log(*a):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s %s():' % (*a,func.__name__))
			
SyntaxError: can use starred expression only as assignment target
>>> def log(text = ''):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s  %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

>>> @log
def now():
	print('123')

	
>>> now()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    now()
TypeError: decorator() missing 1 required positional argument: 'func'
>>>  def log(*a):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s  %s():' % (*a,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

SyntaxError: unexpected indent
>>> def log(*a):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s  %s():' % (*a,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
SyntaxError: can use starred expression only as assignment target
>>> def log(*a):
	list(*a)
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s  %s():' % (*a,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
SyntaxError: can use starred expression only as assignment target
>>> def log(*a):
	list(*a)
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print(*a,'%s():' % (func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
SyntaxError: can use starred expression only as assignment target
SyntaxError: invalid syntax
>>> def log(*a):
	list(*a)
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print(*a,'%s():' % (func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
SyntaxError: only named arguments may follow *expression
>>> def log(*a):
	list(*a)
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print(*a'%s():' % (func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
SyntaxError: invalid syntax
>>> def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s  %s():' % (text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

>>> def log():
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s():' % (func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		def a():
			a = func(*args,**kw)
			print('end call')
			return a
	return wrapper

>>> @log()
def now():
	print('2015')

	
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    @log()
TypeError: log() missing 1 required positional argument: 'func'
>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		def a():
			a = func(*args,**kw)
			print('end call')
			return a(*args,**kw)
	return wrapper

>>> @log()
def now():
	print('2015')

	
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    @log()
TypeError: log() missing 1 required positional argument: 'func'
>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper

>>> @log()
def now():
	print('2015')

	
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    @log()
TypeError: log() missing 1 required positional argument: 'func'
>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	return wrapper

>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		def a():
			a = func(*args,**kw)
			print('end call')
			return a(*args,**kw)
	return wrapper

>>> @log
def now():
	print('2015')

	
>>> now()
call now():
>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		def a():
			a = func(*args,**kw)
			print('end call')
			return a(*args,**kw)
	return wrapper

>>> @log
def now():
	print('2015')

	
>>> now()
call now():
>>> def log(func):
	def wrapper(*args,**kw):		
		def a(*args,**kw):
			print('call %s():' % func.__name__)
			a = func(*args,**kw)
			print('end call')
			return a(*args,**kw)
	return wrapper

>>> @log
def now():
	print('2015')

	
>>> now()
>>> now
<function log.<locals>.wrapper at 0x023AFDB0>
>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		a = func(*args,**kw)
		print('end call')
		return a(*args,**kw)
	return wrapper

>>> @log
def now():
	print('2015')

	
>>> now()
call now():
2015
end call
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    now()
  File "<pyshell#98>", line 6, in wrapper
    return a(*args,**kw)
TypeError: 'NoneType' object is not callable
>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		a(*args,**kw) = func(*args,**kw)
		print('end call')
		return a(*args,**kw)
	return wrapper
SyntaxError: can't assign to function call
>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		a = func
		print('end call')
		return a(*args,**kw)
	return wrapper

>>> @log
def now():
	print('2015')

	
>>> now()
call now():
end call
2015
>>> def log(func):
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	def a():
		a = wrapper
		print('end call')
	return a(*args,**kw)

>>> @log
def now():
	print('2015')

	
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    @log
  File "<pyshell#112>", line 8, in log
    return a(*args,**kw)
NameError: name 'args' is not defined
>>> @log
def now():
	print('2015')

	
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    @log
  File "<pyshell#112>", line 8, in log
    return a(*args,**kw)
NameError: name 'args' is not defined
>>> def log(func):
	def a():
		def wrapper(*args,**kw):
			print('call %s():' % func.__name__)
			return func(*args,**kw)
		print('end call')
	return a

>>> 
>>> @log
def now():
	print('2015')

	
>>> now()
end call
>>> def log(func):
	def a():
		def wrapper(*args,**kw):
			print('call %s():' % func.__name__)
			return func(*args,**kw)
		print('end call')
		return wrapper
	return a

>>> @log
def now():
	print('2015')

	
>>> now()
end call
<function log.<locals>.a.<locals>.wrapper at 0x023AFED0>
>>> def log(func):
	def a():
		def wrapper(*args,**kw):
			print('call %s():' % func.__name__)
			return func(*args,**kw)
		print('end call')
		return wrapper
	return a

>>> def log(func):
	@functools.wrap(func)
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	print('end call')
	return

>>> @log
def now():
	print('201508')

	
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    @log
  File "<pyshell#136>", line 2, in log
    @functools.wrap(func)
AttributeError: 'module' object has no attribute 'wrap'
>>> def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		return func(*args,**kw)
	print('end call')
	return

>>> @log
def now():
	print('201508')

	
end call
>>> now()
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    now()
TypeError: 'NoneType' object is not callable
>>> a()
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    a()
NameError: name 'a' is not defined
>>> def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print('call %s():' % func.__name__)
		temp = func(*args,**kw)
		print('end call')
		return
	return wrapper

>>> @log
def now():
	print('201508')

	
>>> now()
call now():
201508
end call
>>> def log(text):
	@functools.wraps(func)
	if len(text)>0:
		
SyntaxError: invalid syntax
>>> def log(text):
	if len(text) == 0:
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('call %s():' % func.__name__)
			return func(*args,**kw)
		return wrapper
	else:
		def decrator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('%s %s():' % (text,func.__name__))
				return func(*args,**kw)
			return wrapper
		return decrator

	
>>> @log
def now():
	print('201508')

	
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    @log
  File "<pyshell#170>", line 2, in log
    if len(text) == 0:
TypeError: object of type 'function' has no len()
>>> def log(text):
	if isinstance(text ,str) :
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('call %s():' % func.__name__)
			return func(*args,**kw)
		return wrapper
	else:
		def decrator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('%s %s():' % (text,func.__name__))
				return func(*args,**kw)
			return wrapper
		return decrator

	
>>> @log
def now():
	print('201508')

	
>>> now()
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    now()
TypeError: decrator() missing 1 required positional argument: 'func'
>>> def log(text):
	if isinstance(text ,str) is False :
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('call %s():' % func.__name__)
			return func(*args,**kw)
		return wrapper
	else:
		def decrator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('%s %s():' % (text,func.__name__))
				return func(*args,**kw)
			return wrapper
		return decrator

>>> @log
def now():
	print('201508')

Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    @log
  File "<pyshell#180>", line 3, in log
    @functools.wraps(func)
NameError: name 'func' is not defined
>>> def log(text):
	if isinstance(text ,str) is False :
		@functools.wraps(text)
		def wrapper(*args,**kw):
			print('call %s():' % func.__name__)
			return text(*args,**kw)
		return wrapper
	else:
		def decrator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('%s %s():' % (text,func.__name__))
				return func(*args,**kw)
			return wrapper
		return decrator

	
>>> @log
def now():
	print('201508')

	
>>> now()
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    now()
  File "<pyshell#183>", line 5, in wrapper
    print('call %s():' % func.__name__)
NameError: name 'func' is not defined
>>> def log(text):
	if isinstance(text ,str) is False :
		@functools.wraps(text)
		def wrapper(*args,**kw):
			print('call %s():' % text.__name__)
			return text(*args,**kw)
		return wrapper
	else:
		def decrator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print('%s %s():' % (text,func.__name__))
				return func(*args,**kw)
			return wrapper
		return decrator

	
>>> @log
def now():
	print('201508')

	
>>> now()
call now():
201508
>>> @log2('do')
def now():
	print('201508')

	
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    @log2('do')
NameError: name 'log2' is not defined
>>> @log('do')
def now():
	print('201508')

	
>>> now()
do now():
201508
>>> int('123456789')
123456789
>>> int('123456789',base = 8)
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    int('123456789',base = 8)
ValueError: invalid literal for int() with base 8: '123456789'
>>> int('123456789',base=8)
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    int('123456789',base=8)
ValueError: invalid literal for int() with base 8: '123456789'
>>> import functools
>>> int('123',base=8)
83
>>> int('123456789',base=8)
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    int('123456789',base=8)
ValueError: invalid literal for int() with base 8: '123456789'
>>> int(123.23)
123
>>> int('123.23')
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    int('123.23')
ValueError: invalid literal for int() with base 10: '123.23'
>>> t = '123.23'
>>> t
'123.23'
>>> list(t)
['1', '2', '3', '.', '2', '3']
>>> list(t)[::-1]
['3', '2', '.', '3', '2', '1']
>>> t[::]
'123.23'
>>> t[::-1]
'32.321'
>>> int(float('123.23'))
123
>>> int('123456456')
123456456
>>> int('123456456455646546546')
123456456455646546546
>>> int('123456',base=8)
42798
>>> int('1234567',base=8)
342391
>>> int('12345678',base=8)
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    int('12345678',base=8)
ValueError: invalid literal for int() with base 8: '12345678'
>>> int('12345675461354125412',base=8)
188231827468626698
>>> int('4154651',base=16)
68503121
>>> int('15',base=16)
21
>>> def int2(x,base=2):
	return int(x,base)

>>> int2('11111')
31
>>> int2
<function int2 at 0x024C8540>
>>> def int2(x):
	return int(x,base = 2)

>>> def int2('11111')
SyntaxError: invalid syntax
>>> int2('11111')
31
>>> functools.partial
<class 'functools.partial'>
>>> int2(x,base = 10)
Traceback (most recent call last):
  File "<pyshell#233>", line 1, in <module>
    int2(x,base = 10)
NameError: name 'x' is not defined
>>> int2('123',base=10)
Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    int2('123',base=10)
TypeError: int2() got an unexpected keyword argument 'base'
>>> int2= functools.partial(int,base=2)
>>> int2
functools.partial(<class 'int'>, base=2)
>>> int2('10010')
18
>>> kw = {'base':2}
>>> int('10010',**kw)
18
>>> s = int(x,**kw)
Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    s = int(x,**kw)
NameError: name 'x' is not defined
>>> max2 = functools.partial(max,10)
>>> max(2,3,5)
5
>>> max2(2,3,5,1)
10

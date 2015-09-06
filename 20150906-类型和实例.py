Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Student(object):
	pass

>>> s = Student()
>>> s.name = 'Michael'
>>> s.name = 'Samuel'
>>> print (s.name)
Samuel
>>> def set_age(self,age):
	self.age = age

	
>>> from types import MethodType
>>> s.set_age = MethodType(set_age,s,Student)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.set_age = MethodType(set_age,s,Student)
TypeError: method expected 2 arguments, got 3
>>> s.set_age = MethodTyoe(set_age,s.Student)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.set_age = MethodTyoe(set_age,s.Student)
NameError: name 'MethodTyoe' is not defined
>>> s.set_age = MethodType(set_age,s)
>>> s.set_age(25)
>>> s.set_age
<bound method Student.set_age of <__main__.Student object at 0x023586B0>>
>>> a.age
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.age
NameError: name 'a' is not defined
>>> s.age
25
>>> 

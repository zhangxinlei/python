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
>>> s2 = Student()
>>> s2.set_age(26)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s2.set_age(26)
AttributeError: 'Student' object has no attribute 'set_age'
>>> def set_score(self,score:)
SyntaxError: invalid syntax
>>> def set_score(self,score):
	self.score = score

	
>>> Student.set_score = MethodType(set_score,Student)
>>> s2.set_score(99)
>>> s.set_scire(100)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    s.set_scire(100)
AttributeError: 'Student' object has no attribute 'set_scire'
>>> s.set_score(100)
>>> s.score
100
>>> s2.score
100
>>> s2.set_score(99)
>>> s2.score
99
>>> s.score
99
>>> s.set_score
<bound method type.set_score of <class '__main__.Student'>>
>>> s2.set_score
<bound method type.set_score of <class '__main__.Student'>>
>>> class Student(object):
	__slots__ = ('name','age')

	
>>> s= Student()
>>> s.name = 'Michael'
>>> s.age = 25
>>> s.score = 99
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s.score = 99
AttributeError: 'Student' object has no attribute 'score'
>>> class graduateStudent(Student):
	pass

>>> g = gtaduateStudent()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    g = gtaduateStudent()
NameError: name 'gtaduateStudent' is not defined
>>> g = graduateStudent(Student):
	
SyntaxError: invalid syntax
>>> g = gtaduateStudent(Student)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    g = gtaduateStudent(Student)
NameError: name 'gtaduateStudent' is not defined
>>> g = gradunateStudent(Student)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    g = gradunateStudent(Student)
NameError: name 'gradunateStudent' is not defined
>>> g = graduateStudent(Student)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    g = graduateStudent(Student)
TypeError: object() takes no parameters
>>> g =graduateStudent()
>>> g.score = 999
>>> g.score
999
>>> s = Student()
>>> s.score = 8888
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s.score = 8888
AttributeError: 'Student' object has no attribute 'score'
>>> class Student(object):
	def get_score(self):
		return self._score
	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value <0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value

		
>>> s = Student()
>>> s.set_score(60)
>>> s.get_score()
60
>>> s.set_score(999)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.set_score(999)
  File "<pyshell#64>", line 8, in set_score
    raise ValueError('score must between 0~100!')
ValueError: score must between 0~100!
>>> class Student(object):
	@property
	def score(self):
		return self.score
	@score.stter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value

		
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    class Student(object):
  File "<pyshell#80>", line 5, in Student
    @score.stter
AttributeError: 'property' object has no attribute 'stter'
>>> class Student(object):
	@property
	def score(self):
		return self.score
	
	@score.stter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value

		
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    class Student(object):
  File "<pyshell#82>", line 6, in Student
    @score.stter
AttributeError: 'property' object has no attribute 'stter'
>>> class Student(object):
	@property
	def score(self):
		return self.score

	
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value

		
>>> class Student(object):
	@property
	def score(self):
		return self.score
	
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value

		
>>> class Student(object):
	@property
	def score(self):
		return self.score

	@score.stter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value

		
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    class Student(object):
  File "<pyshell#88>", line 6, in Student
    @score.stter
AttributeError: 'property' object has no attribute 'stter'
>>> class Student(object):
	@property
	def score(self):
		return self.score

	
	@score.stter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value

		
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    class Student(object):
  File "<pyshell#90>", line 7, in Student
    @score.stter
AttributeError: 'property' object has no attribute 'stter'
>>> 

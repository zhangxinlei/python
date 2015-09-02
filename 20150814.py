Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> std1 = {'name':'Michael','score'}
SyntaxError: invalid syntax
>>> std1 = {'name':'Michael','score':98}
>>> srd2 = {'name':'Bob','score':81}
>>> def print_score(std):
	print '%s:%s' %(srd['name'],std['score'])
	
SyntaxError: invalid syntax
>>> def print_score(std):
	print '%s: %s' % (std['name'],std['score'])
	
SyntaxError: invalid syntax
>>> std2 = {'name':'Bob','score':81}
>>> def print_score(std):
	print '%s: %s' % (std['name'],std['score'])
	
SyntaxError: invalid syntax
>>> def print_score(std):
	print '%s: %s' % (std['name'], std['score'])
	
SyntaxError: invalid syntax
>>> std1 = { 'name': 'Michael', 'score': 98 }
>>> std2 = { 'name': 'Bob', 'score': 81 }
>>> def print_score(std):
	print '%s: %s' % (std['name'], std['score'])
	
SyntaxError: invalid syntax
>>> def print_score(std):
	print ('%s: %s') % (std['name'], std['score'])

	
>>> print_score(std1)
%s: %s
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print_score(std1)
  File "<pyshell#14>", line 2, in print_score
    print ('%s: %s') % (std['name'], std['score'])
TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple'
>>> def print_score(std):
	print (('%s: %s') % (std['name'], std['score']))

	
>>> print_score(std1)
Michael: 98
>>> print_score(std2)
Bob: 81
>>> class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s : %s') %(self.name,self.score)

		
>>> bart = Student('Bart Simpson',59)
>>> lisa = Student('Lisa Simpsin',87)
>>> bart.print_score()
%s : %s
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    bart.print_score()
  File "<pyshell#26>", line 6, in print_score
    print('%s : %s') %(self.name,self.score)
TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple'
>>> class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s : %s' %(self.name,self.score))

		
>>> bart.print_score()
%s : %s
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    bart.print_score()
  File "<pyshell#26>", line 6, in print_score
    print('%s : %s') %(self.name,self.score)
TypeError: unsupported operand type(s) for %: 'NoneType' and 'tuple'
>>> bart = Student('Bart Simpson',59)
>>> bart.print_score()
Bart Simpson : 59
>>> class Student(object):
	pass

>>> bart = student()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    bart = student()
NameError: name 'student' is not defined
>>> bart = Student()
>>> bart
<__main__.Student object at 0x0238D4D0>
>>> Student
<class '__main__.Student'>
>>> bart.name = 'Bart Simpson'
>>> bart,name
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    bart,name
NameError: name 'name' is not defined
>>> bart.name
'Bart Simpson'
>>> class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score

		
>>> bart = Student('Bart Simpson', 59)
>>> bart.name
'Bart Simpson'
>>> bart.score
59
>>> def print_score(std):
	print('%s:%s' %(std.name,std.score))

	
>>> print_score(bart)
Bart Simpson:59
>>> class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score

		
>>> class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_score(self):
		print ('%s :%s' %(self.name,self.score))

		
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> bart.print_score
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    bart.print_score
AttributeError: 'Student' object has no attribute 'print_score'
>>> class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_score(self):
		print ('%s :%s' %(self.name,self.score))

		
>>> Student
<class '__main__.Student'>
>>> bart.print_score()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    bart.print_score()
AttributeError: 'Student' object has no attribute 'print_score'
>>> class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s :%s' %(self.name,self.score))
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

		
>>> bart.get_grade()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    bart.get_grade()
AttributeError: 'Student' object has no attribute 'get_grade'
>>> bart = Student('Bart Simpson',59)
>>> bart.get_grade()
'C'
>>> bart.name
'Bart Simpson'
>>> bart.print_score()
Bart Simpson :59
>>> bart = Student('Bart Simpson',98)
>>> bart.score
98
>>> bart.score = 59
>>> bart.score
59
>>> class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print ('%s :%s' %(self.__name,self.__score))

		
>>> bart = Student('Bart Simpson',98)
>>> bart.__name
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    bart.__name
AttributeError: 'Student' object has no attribute '__name'
>>> class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print ('%s :%s' %(self.__name,self.__score))
	def get_name(self):
		return self.__name
	def ger_score(self):
		return self.__score

	
>>>  class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print ('%s :%s' %(self.__name,self.__score))
	def get_name(self):
		return self.__name
	def ger_score(self):
		return self.__score
	
SyntaxError: unexpected indent
>>> class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print ('%s :%s' %(self.__name,self.__score))
	def get_name(self):
		return self.__name
	def ger_score(self):
		return self.__score
	def set_score(self, score):
		self.__score = score

		
>>> class Student(object):
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print ('%s :%s' %(self.__name,self.__score))
	def get_name(self):
		return self.__name
	def ger_score(self,score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

		
>>> bart.__name
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    bart.__name
AttributeError: 'Student' object has no attribute '__name'
>>> bart._Student__name
'Bart Simpson'
>>> class Animal(object):
	def run(self):
		print 'Animal is running...'
		
SyntaxError: Missing parentheses in call to 'print'
>>> class Animal(object):
	def run(self):
		print('Animal is running...')

		
>>> class Dog(Animal):
	pass

>>> class Cat(Animal):
	pass

>>> dog = Dog()
>>> dog.run()
Animal is running...
>>> cat = Cat()
>>> cat.run
<bound method Cat.run of <__main__.Cat object at 0x0243D570>>
>>> cat.run()
Animal is running...
>>> class Dog(Animal):
	def run(self):
		print 'Dog is running...'
		
SyntaxError: Missing parentheses in call to 'print'
>>> class Dog(Animal):
	def run(self):
		print('Dog is running......')
class Cat(Animal):
	
SyntaxError: invalid syntax
>>> class Dog(Animal):
	def run(self):
		print('Dog is running......')

		
>>> class Cat(Animall):
	def run(self):
		print('Cat is running......')

		
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    class Cat(Animall):
NameError: name 'Animall' is not defined
>>> class Cat(Animal):
	def run(self):
		print('Cat is running......')

		
>>> dog.run
<bound method Dog.run of <__main__.Dog object at 0x0238D9B0>>
>>> dog.run()
Animal is running...
>>> dog = Dog()
>>> dog.run()
Dog is running......
>>> b = Animal()
>>> isinstance(b,Animal)
True
>>> c = Dog()
>>> isinstance(c,Dog)
True
>>> isinstance(c,Animal)
True
>>> b = Animal()
>>> b
<__main__.Animal object at 0x0238D9B0>
>>> isinstance(b,Dog)
False
>>> isinstance(b,Animal)
True
>>> def run_twice(animal):
	animal.run()
	animal.run()

	
>>> run_twice(Animal())
Animal is running...
Animal is running...
>>> run_twice(animal())
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    run_twice(animal())
NameError: name 'animal' is not defined
>>> run_twice(Dog())
Dog is running......
Dog is running......
>>> run_twice(Cat())
Cat is running......
Cat is running......
>>> class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')

		
>>> run_twice(Tortoise())
Tortoise is running slowly...
Tortoise is running slowly...
>>> class T(int):
	def run(self):
		print('Tortoise is running slowly...')

		
>>> run_twice(T())
Tortoise is running slowly...
Tortoise is running slowly...
>>> T
<class '__main__.T'>
>>> Tortoise
<class '__main__.Tortoise'>
>>> Animal
<class '__main__.Animal'>
>>> isinstance(T,Animal)
False
>>> isinstance(Tortoise,Animal)
False
>>> Animal
<class '__main__.Animal'>
>>> isinstance(Dog,Animal)
False
>>> t = T()
>>> t
0
>>> isinstance(T,Animal)
False
>>> isinstance(t,Animal)
False
>>> isinstance(t,int)
True
>>> f = Tortoise()
>>> isinstance(f,Animal)
True
>>> 

Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Student(object):

	@property
	def birth(self):
		return self._birth

>>> class Student(object):

	@property
	def birth(self):
		return self._birth
	@
	
SyntaxError: invalid syntax
>>> class Student(object):

	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self,value):
		self._birth = value

	@property
	def age(self):
		return 2015 - self._birth

	
>>> class Student(object):
	@property
	def birth(self):
		return self._birth
	@birth.setter
	def birth(self,value):
		self._birth = value
	@property
	def age(self):
		return 2015 - self._birth

	
>>> class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self,value):
		self._width = value
	@property
	def height(self):
		return self._height
	@height.setter
	def height(self,value):
		self._height = value
	@property
	def resolution(self):
		return self.width * self.height

	
>>> s = Screen()
>>> s.width = 1024
>>> s.height = 798
>>> print(s.resolution)
817152
>>> 

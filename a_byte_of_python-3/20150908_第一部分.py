Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('Hello World')  #注意print是一个函数
Hello World
>>> a = 52.3E-4
>>> a
0.00523
>>> #注意科学计数法的应用
>>> a = '空格会保留    ！    '
>>> a
'空格会保留    ！    '
>>> #用三重引号制定多行字符串
>>> '''line1
line2
line3
...
linen
'''
'line1\nline2\nline3\n...\nlinen\n'
>>> a = '''line1
line2
line3
...
linen
'''
>>> a
'line1\nline2\nline3\n...\nlinen\n'
>>> print(a)
line1
line2
line3
...
linen

>>> #单双引号是相同的
>>> #标识符、变量需要以字母或_开头
>>> 12a = 20
SyntaxError: invalid syntax
>>> a12 = 20
>>> a12
20
>>> name = a
>>> nAme = a12
>>> [name,nAme]
['line1\nline2\nline3\n...\nlinen\n', 20]
>>> s = '这是一个字符串。 \
用了反斜杠在继续'
>>> s
'这是一个字符串。 用了反斜杠在继续'
>>> print(a)
line1
line2
line3
...
linen

>>> print\
(a)
line1
line2
line3
...
linen

>>> 
print(
	a
	)
line1
line2
line3
...
linen

>>> i = 5
>>>  print(i) #开头有空格
 
SyntaxError: unexpected indent
>>> print('Next cheapt 操作对象')
Next cheapt 操作对象
>>> 

Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ##用；来分隔逻辑行，用/来连接逻辑行
>>> ##操作对象
>>> 2+3
5
>>> 3*5
15
>>> #+
>>> 3+2
5
>>> a+b
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a+b
NameError: name 'a' is not defined
>>> 'a'+'b'
'ab'
>>> #	-
>>> -5.2
-5.2
>>> 50-24
26
>>> # *
>>> 2*3
6
>>> 'la'*3
'lalala'
>>> 
>>> #**
>>> 3**4
81
>>> 3*3*3*3
81
>>> # /
>>> 4/3
1.3333333333333333
>>> # //整除
>>> 4//3
1
>>> # %余数
>>> 8%3
2
>>> -25.5 % 2.25
1.5
>>> # <<左移
>>> 2<<2
8
>>> # >>右移
>>> 11>>5
0
>>> 11>>1
5
>>> # 位相与
>>> 5&3
1
>>> # 位或与
>>> 5|3
7
>>> # 位异或^
>>> 5^3
6
>>> # 位求反~
>>> ~5
-6
>>> ~x
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    ~x
NameError: name 'x' is not defined
>>> ~'x'
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    ~'x'
TypeError: bad operand type for unary ~: 'str'
>>> #~x == -（x+1）
>>> #<
>>> 5<3
False
>>> 3<5
True
>>> 3<5<7
True
>>> #	>
>>> 5>3
True
>>> #	<=
>>> 3<=3
True
>>> #	>=
>>> 3>=3
True
>>> # ==
>>> 3 == 3
True
>>> 'str' == 'stR'
False
>>> #	!= 不等于
>>> 2 != 3
True
>>> # not逻辑非
>>> not True
False
>>> not False
True
>>> # and 逻辑与
>>> False and 'any'
False
>>> 'any' and False
False
>>> #	or
>>> True or False
True
>>> True or 'any'
True
>>> #赋值
>>> a = 2
>>> a *= 3  #就是a = a*3
>>> a
6
>>> # var = var operation expression	写成 var operation= expression
>>> a = 1;b=2;c=3
>>> a,b,c
(1, 2, 3)
>>> a = b = c #a=(b=c)
>>> a
3
>>> #控制流语句
>>> #if
>>> 

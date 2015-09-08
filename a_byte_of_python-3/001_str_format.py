#coding=utf-8 
age = 20
name = 'Swaroop'

print('{0} was {1} years old when he wrote this book' . format(name,age))
print('Why is {0} playing with that python?' . format(name))

#下面是我个人的做法
print('Another way:')
print('%s was %s years old when he worte this bool' % (name,age))
print('Why is %s playing with that python?' % name)

input()

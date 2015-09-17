#coading=utf-8

number = 23
guess = int(input('请输入一个整数:'))

if guess == number:
	print('恭喜，你猜对了')
	print('但你没有获得任何奖品')
	
elif guess < number:
	print('不对，你猜的有点儿小')
else:
	print('不对，你猜的有点大')

print('完成')

input()

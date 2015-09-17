#coading=utf-8

number = 23
running = True 

while running:
	guess = int(input('输入一个整数：'))
	
	if guess == number:
		print('恭喜你，猜对了')
		running = False #停止
	elif guess < number:
		print('不对，猜得有点小')
	else:
		print('不对，猜的有点大')
else:
	print('循环结束')

print('完成')
input()

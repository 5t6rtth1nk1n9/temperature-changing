import random
start = input('請輸入隨機數字最小範圍:')
end = input('請輸入隨機數字最大範圍:')
r = random.randint(int(start),int(end))
count = 1
while True:
	print('這是你猜的第',count,'次喔!')
	number = input('請輸入你認為正確的數字:')
	count = count + 1
	if r == int(number):
		print('~恭喜猜中正確答案~')
		break
	elif r > int(number):
		print('猜得太小搂重猜一遍吧!')
	else:
		print('猜得太大搂重猜一遍吧!')

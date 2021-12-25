print('歡迎使用此BMI計算機')
height = input('請輸入您的身高(cm): ')
weight = input('請輸入您的體重(kg): ')
weight = float(weight)
height = float(height)
BMI = (weight) / (height/100)**2
BMI = round(BMI,4)
print('你的BMI為', BMI)
if BMI <= 18.5:
	print('你過輕了喔')
elif 18.5 <= BMI <= 24:
	print('你的體重剛剛好')
elif 24 <= BMI <= 27:
	print('你過重了')
elif 27 <= BMI <= 30:
	print('輕度肥胖')
elif 30 <= BMI <= 35:
	print('中度肥胖')
else:
	print('重度肥胖')

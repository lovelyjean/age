driving = input('請問你有沒有開過車? ')
if driving != 'yes' and driving != 'no':
	print('only yes or no')
	raise SystemExit

age = input('請問你的年齡? ')
age = int(age)

if driving == 'yes':
	if age >= 18:
		print('passed')
	else:
		print('奇怪 你怎麼會有開過車')
elif driving == 'no':
	if age >= 18:
		print('你可以考駕照了啊 怎麼還不去考')
	else:
		print('很好 再過幾年就可以考駕照了')
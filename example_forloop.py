for letter in 'Happiness':
   print(letter)
##-------------------------------------------------------------------##
fruits = ['banana','pineapple','apple']

for fruit in fruits:
    print(fruit)
##-------------------------------------------------------------------##

fruits = ['banana', 'apple', 'pineapple']
count = 0
for index in range(len(fruits)):
	count += 1
	print('#{} : {}'.format(count,fruits[index]))
  
##-------------------------------------------------------------------##

for num1 in range(0,10):
	for num2 in range(2,num1):
		if num1 % num2 == 0:
			num3 = num1 / num2
			print('{} equals to {} * {}.'.format(num1,num2,num3))
			break
	else:
		print(num1, ' is a prime number.')

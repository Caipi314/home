product = int(input('Enter product: '))
sum = int(input('Enter sum: '))

for i in range(-10000, 10000):
	for j in range(-10000, 10000):
		if i * j == product and i + j == sum:
			exit((i, j));
print('NOPE doesnt work')
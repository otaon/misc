# 95422357545868773174
# 9  22357545868773174	(54)
# 9  2  57545868773174	(23)
# 9  2  575  868773174	(45)
# 9  2  575  86  73174	(87)
# 9  2  575  8    3174	(67)


dataset = []
try:
	while True:
		dataset.append(input().strip().upper() + 'a')
except EOFError:
	pass

for data in dataset:
	index = 0
	while data[index + 1] != 'a':
		if int(data[index]) - int(data[index + 1]) == 1 \
		or int(data[index]) - int(data[index + 1]) == -1:
			data = data[:index] + data[index + 2:]
			if index != 0:	index -= 1
		else:
			index += 1
	print(data[:-1])

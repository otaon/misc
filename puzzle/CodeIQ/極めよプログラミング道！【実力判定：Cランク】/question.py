dataset = []
try:
	while True:
		dataset.append(input().strip().upper())
except EOFError:
	pass

for i in range(len(dataset)):
	dataset[i] = sorted(list(dataset[i]))
	if len(dataset[i]) == 4:
		if dataset[i][0] == '0':
			print(dataset[i][1])
		else:
			print(dataset[i][-1])
	else:
		print("error")


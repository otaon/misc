dataset = []
try:
	while True:
		dataset.append(int(input().strip().upper()))
except EOFError:
	pass

MAX = 1999999
for data in dataset:
	if data % 2 == 0:
		print(0)
	else:
		num_N = MAX // data
		if num_N % 2 == 0:
			print(num_N // 2)
		else:
			print(num_N // 2 + 1)

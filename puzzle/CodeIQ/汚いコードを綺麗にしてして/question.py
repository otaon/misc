align = input().lower()
dataset = []
for i in range(3):
	dataset.append(input().strip())

val_lens = []
for i in range(len(dataset)):
	val_lens.append(dataset[i].index('='))

max_val_lens = max(val_lens)


if align == 'l':
	for i in range(len(dataset)):
		print(dataset[i][:val_lens[i]], end = '')
		print('.' * (max_val_lens - val_lens[i]), end = '')
		print(dataset[i][val_lens[i]:])
elif align == 'r':
	for i in range(len(dataset)):
		print('.' * (max_val_lens - val_lens[i]), end = '')
		print(dataset[i][:val_lens[i]], end = '')
		print(dataset[i][val_lens[i]:])

Nset = []
try:
	while True:
		Nset.append(int(input().strip().upper()))
except EOFError:
	pass

SUM_MAX = 1999999	# "連続した2値の合計"の最大値
for N in Nset:
	if N % 2 == 0:
		# ある整数Nが偶数の場合、連続した2値がNの倍数となる組み合わせは0個で確定
		print(0)
	else:
		# ある整数Nが奇数の場合、Nの倍数は偶奇を繰り返す
		# そのうち、奇数であるもののみ"連続した2値の合計"に含まれる
		count = SUM_MAX // N
		if count % 2 == 0:
			print(count // 2)
		else:
			print(count // 2 + 1)

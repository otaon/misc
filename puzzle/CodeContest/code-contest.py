#########################################################################
## コードコンテスト問題
#########################################################################
# XさんとYさんが1つのケーキを分け合う。
# ケーキは円形である。
# 最初に、ケーキをN個に切り分ける。
# (N | 1 <= N <= 2000)
# 切り分け方は、放射線状である。
# これらの各ピースに番号iをつける。
# 番号iは、あるピースを1としたら、そこから反時計回りに1ずつ増加させる。
# (i | 1 <= i <= N)
# また、切り分けたピースは全て異なる大きさA_iである。
# (A_i | 1 <= A_i <= 1000000000)
# 下記ルールによってケーキを交互に分け合う。
#   1. 最初に、Xさんが好きなピースを取る。このピースをT_X1とする。
#   2. Yさんは、取れるピースのうち一番大きいものを取る。
#   3. Xさんは、取れるピースのうち好きなものを取る。
#   4. 上記2.3.をケーキがなくなるまで繰り返す。
# このとき、Xさんが取るピースの大きさの合計が最も大きくなるようにしたい。
# そうなるとき、Xさんが取るピースの合計はいくつになるか求めよ。
#########################################################################

#def estimateBenefit(pieces):
#	print(pieces)
#
#	benefit_head = 0	# X takes the piece at the head
#	benefit_tail = 0	# X takes the piece at the tail
#
#	if len(pieces) >= 1:	# the cake is not empty now
#		benefit_head = pieces[0]	# X takes the piece at the head
#		benefit_tail = pieces[-1]	# X takes the piece at the tail
#
#		if len(pieces) >= 2:
#			if pieces[1] > pieces[-1]:
#				benefit_head += estimateBenefit(pieces[2:])		# Y takes the piece at the head
#			else:
#				benefit_head += estimateBenefit(pieces[1:-1])	# Y takes the piece at the tail
#
#			if pieces[0] > pieces[-2]:
#				benefit_tail += estimateBenefit(pieces[1:-1])	# Y takes the piece at the head
#			else:
#				benefit_tail += estimateBenefit(pieces[:-2])		# Y takes the piece at the tail
#
#	benefit_temp = max(benefit_head, benefit_tail)
#	print('now you earn ', benefit_temp)
#	return benefit_temp

#def estimateBenefit(pieces):
#	pieces_x_takes_head, pieces_x_takes_tail = (pieces.copy(), pieces.copy())
#	benefit_head = benefit_tail = 0
#
#	# X's turn
#	if len(pieces) >= 1:
#		benefit_head += pieces_x_takes_head.pop(0)	# X takes the piece at the head
#		benefit_tail += pieces_x_takes_tail.pop(-1)	# X takes the piece at the tail
#
#	# Y's turn
#	if len(pieces) >= 2:
#		if pieces_x_takes_head[0] > pieces_x_takes_head[-1]:
#			pieces_x_takes_head.pop(0)	# Y takes the piece at the head
#		else:
#			pieces_x_takes_head.pop(-1)	# Y takes the piece at the tail
#
#		if pieces_x_takes_tail[0] > pieces_x_takes_tail[-1]:
#			pieces_x_takes_tail.pop(0)	# Y takes the piece at the head
#		else:
#			pieces_x_takes_tail.pop(-1)	# Y takes the piece at the tail
#
#		# there is the cake still left
#		benefit_head += estimateBenefit(pieces_x_takes_head)
#		benefit_tail += estimateBenefit(pieces_x_takes_tail)
#
#	return max(benefit_head, benefit_tail)

def estimateBenefit(pieces):
	pieces_x_takes_head, pieces_x_takes_tail = (pieces.copy(), pieces.copy())
	benefit_head = benefit_tail = 0

	if len(pieces) >= 1:
		benefit_head += pieces_x_takes_head.pop(0)	# X takes the piece at the head
		benefit_tail += pieces_x_takes_tail.pop(-1)	# X takes the piece at the tail

	if len(pieces) >= 2:
		pieces_x_takes_head.pop(0 if (pieces_x_takes_head[0] > pieces_x_takes_head[-1]) else -1)
		pieces_x_takes_tail.pop(0 if (pieces_x_takes_tail[0] > pieces_x_takes_tail[-1]) else -1)
		
		benefit_head += estimateBenefit(pieces_x_takes_head)
		benefit_tail += estimateBenefit(pieces_x_takes_tail)
	
	return max(benefit_head, benefit_tail)


#########################################################################
# main
#########################################################################
print('Input number of pieces of cake')
num_piece = input('>> ')
print('You will cut the cake into ', num_piece)

print('tell me each size of piece of the cake')
piece_sizes = [int(input('>> ')) for i in range(int(num_piece))]
print('each size of piece of the cake is: ', piece_sizes)

max_benefit = 0
for i in range(len(piece_sizes)):
	print('target: ', piece_sizes)
	benefit_temp = estimateBenefit(piece_sizes)
	print('the sum of size that x can take: ', benefit_temp)
	if benefit_temp >= max_benefit:
		max_benefit = benefit_temp
	piece_sizes.append(piece_sizes[0])
	piece_sizes.pop(0)

print('You can take at most', max_benefit)


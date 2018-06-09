dataset = []
try:
	while True:
		dataset.append(list(input().strip().upper()))
except EOFError:
	pass

edgelen = len(dataset)

for i in range(edgelen):
	dataset[i] = list(map(lambda x: int(x), dataset[i]))

routes = [[-1 for i in range(edgelen)] for i in range(edgelen)]

# fill right edge
weight_temp = 0
for y in reversed(range(edgelen)):
	routes[y][edgelen - 1] = weight_temp + dataset[y][edgelen - 1]
	weight_temp = routes[y][edgelen - 1]

# fill bottom edge (right bottom is calced at twice)
weight_temp = 0
for x in reversed(range(edgelen)):
	routes[edgelen - 1][x] = weight_temp + dataset[edgelen - 1][x]
	weight_temp = routes[edgelen - 1][x]

for y in reversed(range(edgelen - 1)):
	for x in reversed(range(edgelen - 1)):
		routes[y][x] = dataset[y][x] + min(routes[y + 1][x], routes[y][x + 1])

print(routes[0][0])

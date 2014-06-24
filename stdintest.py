from sys import stdin
def test():
	data = (line for line in stdin.read().splitlines())
	t = int(next(data))
	matrix = []
	rnum = 0
	for i in range(t):
		cnum = 0
		row = []
		for char in next(data):
			row.append(Cell(rnum,cnum,char))
			cnum += 1
		matrix.append(row)
		rnum += 1
	print matrix

test()
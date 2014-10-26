t = input()
for i in xrange(t):
	n = input()
	power = 2**(n-1)
	sum = 0
	for j in xrange(0,n):
		sum += (j+1)*power
	print sum
def sieve(n,result):
	odd = 0
	even = 0
	for i in xrange(n):
		if result[i]%2!=0:
			odd += 1
		else:
			even += 1
	return odd * even
t = input()
for i in xrange(t):
	n = input()
	st = map(int, raw_input().split())
	print sieve(n,st)

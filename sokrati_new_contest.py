from sys import stdin
import math
def cCr(n,r):
	f = math.factorial
	return f(n)/f(r)/f(n-r)

def challenge():
	data = (line for line in stdin.read().splitlines())
	t = int(next(data))
	for t in xrange(t):
		s,n,m,k = map(int,next(data).split())
		probability = 0.000000
		if s == n:
			probability = 1.000000
			break
		elif s > n:
			if n == m:
				probability = 1.000000
				break
			else:
				total = nCr(s,n)
				favorable = nCr(m,k)*nCr((s-m),(n-k))
				probability = favorable/total
		print '{0:.6f}'.format(probability)
challenge()
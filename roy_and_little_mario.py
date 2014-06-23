import math
def nPr(n,r):
	f = math.factorial
	return f(n)/f(n-r)

t = input()
T = t if 1<=t<=10 else exit(1)
for i in xrange(T):
	n = input()
	N = n if 1<=n<=10**5 else exit(1)
	
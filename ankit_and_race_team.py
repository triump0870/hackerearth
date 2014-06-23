import math
def nCr(n,r):
	f = math.factorial
	return f(n)/f(r)/f(n-r)
def error():
	exit(1)

t = input()
T = t if 1<=t<=100 else error()
mod = 1000000007
inf = 2000000000
for i in xrange(T):
	n,k = map(int,raw_input().split())
	l = map(int,raw_input().split())
	
	l.sort()
	
	N = n if 1<=n<=10**5 else error()
	K = k if 1<=k<=N else error()
	sum = 0
	x = nCr(N,K)
	for j in xrange(x):
		l[j] = l[j] if 0<=l[j]<=2*10**9 else error()
		if (N-j-1)>=(K-1):
			w = (l[j]*nCr(N-j-1,K-1)) % mod
			sum += w
		else:
			break
	print sum % mod

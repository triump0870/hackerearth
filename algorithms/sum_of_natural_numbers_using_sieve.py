def natural(n):
	if n <1:
		return 0
	sieve = [0]*(n+1)
	for x in xrange(1,n+1):
		sieve[x]=x*(x+1)/2
	return sieve[1:]
def sum(n):
	naturals = natural(n-1)
	print naturals
	sum = [naturals[i-1] for i in xrange(1,n) if n%i==0]
	print sum
print sum(10)
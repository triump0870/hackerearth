def prime(n):
	if n <= 1:
		return 0
	else:
	    divisors = [ d for d in xrange(2,n+1) if n % d == 0 ]
	    s = [ d for d in divisors if \
	    	all( d % od != 0 for od in divisors if od != d ) ]
	    return min(s)
def natural(n):
	if n<=1:
		return 0
	else:
		s = [d for d in xrange(1,n) if n%d==0]
		print s
		return sum(s)
t= input()
for i in xrange(t):
	n = input()
	s = 0
	for j in xrange(n,1,-1):
		s+= prime(j)+natural(j)
	print s%n

def primefact(n):
	divisors = [d for d in xrange(2,n+1) if n%d==0]
	s = [d for d in divisors if all(d%od!=0 for od in divisors if od!=d)]
	return min(s)
t = input()
for i in xrange(t):
	r = input()
	a = primefact(r)
	b = r-a
	print b
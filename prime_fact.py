def prime(n):
	divisors = [ d for d in xrange(2,n//2+1) if n % d == 0 ]
	print divisors
	t = all( d % od != 0 for od in divisors if od != d )
	
	s = [ d for d in divisors if \
	    	all( d % od != 0 for od in divisors if od != d ) ]
	print t
	print s
	print min(s)

prime(24)

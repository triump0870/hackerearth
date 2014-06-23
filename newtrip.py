import math
import time
import resource
def is_triple(hypotenuse):
    """return (a, b, c) if Pythagrean Triple, else None"""
    if hypotenuse < 4:
        return None

    c = hypotenuse ** 2

    for a in xrange(3, hypotenuse):
        b = math.sqrt(c - (a ** 2)) 
        if b == int(b):
            return a, int(b), hypotenuse

    return None
t = input()
start = time.clock()
T = t if 1<=t<=100 else exit(1)
for i in xrange(t):
	n = input()
	N = n if 1<=n<=10**6 else exit(1)
	count = 0
	for j in xrange(5,n+1):
		if is_triple(j):
			print is_triple(j)
			count += 1
	print count
	elapsed = time.clock() - start
	print "elapsed Time = ",elapsed
	print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
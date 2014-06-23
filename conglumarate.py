import time
import resource
t = input()
start = time.clock()
for i in xrange(t):
	n = input()
	b = [i**2 for i in range(n+1)]
	count = 0
	for k in xrange(1,len(b)+1):
		x = k*3
		y = k*4
		z = k*5
		o = k*12
		p = k*13
		if x<=n and y<=n and z<=n:
			if b[x]+b[y] == b[z]:
				count += 1
		if z<=n and o<=n and p<=n:
			if b[z]+b[o]==b[p]:
				count +=1
	print count
	elp = time.clock() - start
	print "Elapsed Time=",elp
	print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
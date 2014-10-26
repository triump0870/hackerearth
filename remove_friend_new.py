t = input()
for i in xrange(t):
	n,k = map(int,raw_input().split())
	s = raw_input().split()
	pop = {j:int(s[j]) for j in xrange(n)}
	l=0
	while k >0:
		keys = pop.keys()
		print len(keys)
		:
			print "in loop length of keys:",len(keys)
			print "i=%d and j=%d"%(i,j)
			if i < len(keys) - 1 and pop[j] < pop[keys[i+1]]:
				print "pop[j]=",pop[j]
				print "pop[keys[i+1]]=",pop[keys[i+1]]
				del pop[j]
				k -= 1
				break
			else:
				l += 1
	print pop

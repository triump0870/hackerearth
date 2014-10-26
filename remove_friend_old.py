t = input()
for i in xrange(t):
	n,k = map(int,raw_input().split())
	pop = map(int,raw_input().split())
	delfrnd = False
	for j in xrange(k):
		for i in xrange(1,len(pop)):
			if pop[i-1] < pop[i]:
				del pop[i-1]
				delfrnd = True
				break
		if delfrnd == False:
			del pop[-1]

	print ' '.join(str(e) for e in pop)
from sys import stdin
t = input()
for i in xrange(t):
	n = input()
	bullets = 6
	d = stdin.readline().split()
	walker = {j:int(d[j]) for j in xrange(n)}
	while bullets:
		bullets -= 1
		a = min(walker,key=walker.get)
		if walker[a] == 0:
			print "Goodbye Rick"
			print n - len(walker)
			break
	
		del walker[a]
		for k,v in walker.items():
			walker[k] = v - 1
		if bullets == 0 and len(walker):
			bullets = 6
			for k,v in walker.items():
				walker[k] = v - 1
		if len(walker) == 0:
			print "Rick now go and save Carl and Judas"
			break
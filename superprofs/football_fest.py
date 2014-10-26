t = input()
for i in xrange(t):
	l = []
	n,id = map(int,raw_input().split())
	l.append(id)
	curr = l[len(l)-1]
	prev = curr
	for j in xrange(n):
		x = raw_input().split()
		if 'P' in x[0]:
			l.append(x[1])
			prev = curr
			curr = l[len(l)-1]
		else:
			curr, prev = prev, curr

	print "Player %s"%curr


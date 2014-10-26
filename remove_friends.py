t = input()
for z in xrange(t):
	n,m = map(int,raw_input().split())
	s = map(int,raw_input().split())
	d = {j:s[j] for j in xrange(len(s))}
	delfriend = False
	keys = d.keys()
	for i, k in enumerate(keys):
		if i < len(keys) - 1 and d[k]<d[keys[i+1]]:
		    del d[k]
		    delfriend = True
		    break
	if delfriend == False:
		del d[-1]

	print ' '.join(str(e) for e in d.values())
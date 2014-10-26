from itertools import chain,combinations
def subset(n):
	for z in chain.from_iterable(combinations(n,r) for r in xrange(len(n)+1)):
		yield set(z)
t = input()
T = t if 1<=t<=42 else exit()
for t in xrange(T):
	i = input()
	i = set(xrange(1,i+1))
	s = 0
	for i in subset(i):
		s = s + sum(i)
	print s


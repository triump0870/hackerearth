t = input()
for i in xrange(t):
	n = input()
	l = map(int,raw_input().split())
	count = 0
	for j in xrange(n):
		for k in xrange(j+1,n):
			if 1<=l[j]<l[k] and 1<=l[k]<=l[n-1]:
				if (l[j]^l[k])%2 != 0:
					count += 1
	print count

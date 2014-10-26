t  = input()
for i in xrange(t):
	n = input()
	l = map(int,raw_input().split())
	count = 0
	for m in xrange(n):
		j = m
		k = n -1
		while(j<k):
			if (l[j] ^ l[k])%2 != 0:
				count += 1
				j += 1
			else:
				k -= 1
	print count
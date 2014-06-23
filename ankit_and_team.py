def choose(n, k):
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

q = input()
t =q if 1<=q<=100 else exit(1)
for i in range(t):
	n,k = raw_input().split()
	f = int(n)
	n = f if 1<=f<=100000 else exit(1)
	y = int(k)
	l = y if 1<=y<=n else exit(1)
	s = list((raw_input().split()))
	sum = 0
	t = s[:]
	r = choose(n,l)
	for j in range(r):
		print 'j=',j
		print '----------------------------------'
		kt = []
		k = l 
		while (k>0):
			m = t.pop(-1)
			kt.append(m)
			t.insert(0,m)
			k -=1
			print 'inline kt:',kt
			print 'inline t:',t
		x = int(min(kt))
		sum += x
		print kt
		print "minimum:",x
	print sum % 1000000007

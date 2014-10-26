from fractions import gcd
def arjit():
	global a,b
	s = gcd(a,b)
	if s >1:
		if b%s == 0:
			b = b/s 
		else:
			b -= 1
	else:
		b -= 1
	return a,b
	
def chandu():
	global a,b
	s = gcd(a,b)
	if s > 1:
		if a%s == 0:
			a = a/s 
		else:
			a -= 1
	else:
		a -= 1
	return a,b

t = input()
for i in xrange(t):
	global a,b
	a,b = map(int,raw_input().split())
	while a>0 or b >0:
		if a == 1 and b == 1:
			print 'Draw'
			break
		elif a == 1:
			print 'Chandu Don'
			break
		elif b == 1:
			print 'Arjit'
			break
		else:
			if a>1 and b > 1:
				arjit()
			if a>1 and b>1:
				chandu()
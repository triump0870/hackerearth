def prime(n):
	factors = []
	if n % 2==0:
		return 2
	elif n%3==0:
		return 3
	else:
		for i in xrange(5,int(n**0.5)+1,6):
			print i
			if n%i==0:
				factors.append(i)
			if n%(i+2)==0:
				factors.append(i+2)
		return	min(factors) if factors!=[] else n
def natural(n):
	if n<=1:
		return 0
	else:
		s = [d for d in xrange(1,n) if n%d==0]
		return sum(s)
def f(n):
	if n <=1:
		return 0
	else:
		s = f(n-1) + prime(n)
	return s
def g(n):
	if n<=1:
		return 0
	else:
		s = g(n-1) + natural(n)
	return s
t= input()
for i in xrange(t):
	n = input()
	a = (f(n) + g(n))%n
	print a

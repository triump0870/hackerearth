def fact(n):
	factors = []
	if n % 2==0:
		return 2
	elif n%3==0:
		return 3
	else:
		for i in xrange(5,int(n**0.5)+1,6):
			if n%i==0:
				factors.append(i)
			if n%(i+2)==0:
				factors.append(i+2)
		return	min(factors) if factors!=[] else n
	
		
t = input()
for  i in xrange(t):
	r = input()
	print r-fact(r)

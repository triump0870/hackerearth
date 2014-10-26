def prime_fact(n):
	if n<=2:
		return [2]
	sieve = [True]*(n+1)
	for x in xrange(3,int(n**0.5)+1,2):
		for y in xrange(3,(n//x)+1,2):
			sieve[(x*y)]=False
	primes = [2]+[i for i in xrange(3,n//2+1,2) if sieve[i]]
	facts = [i for i in primes if n%i==0]
	return facts if facts!=[] else [n]
 
def smallest_prime_fact(n):
	if n<=1:
		return 0
	facts = prime_fact(n)
	return min(facts) 

def sum_of_naturals(n):
	if n<=1:
		return 0
	sieve = [i*(i+1)/2 for i in xrange(1,n)]
	return sieve[max([i for i in xrange(1,n) if n%i==0])-1]

t = input()
for i in xrange(t):
	n = input()
	sum = 0
	for j in xrange(n,1,-1):
		sum += smallest_prime_fact(j)+sum_of_naturals(j)
	print sum%n
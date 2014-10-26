import time
import doctest

mod = 1000000007
def calculate(n):
	a = [0,1,2,4]
	for i in xrange(4,n+1):
		temp = (a[i-3]+a[i-2]+a[i-1])%mod
		a.append(temp)
	print a[n]
	del a[:]

def main():
	t = input()
	for i in xrange(t):
		n = input()
		start = time.clock()
		print start
		calculate(n)
		print time.clock()
		elp = time.clock()-start
		print "{0:.10f}".format(elp)
if __name__ == "__main__":
	main()
	
doctest.testmod()
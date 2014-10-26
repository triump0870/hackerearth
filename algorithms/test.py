from timeit import Timer
import timeit
arr = [0]*26
f = [0]*26
ans = [0]*26
def mark(a):
	i = 2
	while i*a<=24:
		num = i*a
		if arr[num]==0:
			arr[num] += a
		i += 1
def sieve():
	for i in xrange(2,24):
		if arr[i]==0:
			arr[i] = arr[i-1]+i
			mark(i)
		else:
			arr[i] += arr[i-1]

def main(n):
	sieve()
	for i in xrange(1,26//2+1):
		for j in xrange(i+i,26,i):
			print "i==%d and j==%d"%(i,j)

			f[j] += i
			print "======================="
			print f
			print "======================="

	for i in xrange(2,26):
		ans[i] = ans[i-1]+f[i]
	print (ans[n]+arr[n])%n
if __name__ == '__main__':
	main(20)
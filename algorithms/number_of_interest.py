from timeit import Timer
import timeit
arr = [0]*100005
f = [0]*100005
ans = [0]*100005
def mark(a):
	i = 2
	while i*a<=100002:
		num = i*a
		if arr[num]==0:
			arr[num] += a
		i += 1
def sieve():
	for i in xrange(2,100002):
		if arr[i]==0:
			arr[i] = arr[i-1]+i
			mark(i)
		else:
			arr[i] += arr[i-1]

def main(n):
	sieve()
	for i in xrange(1,100005//2+1):
		for j in xrange(i+i,100005,i):
			f[j] += i

	for i in xrange(2,100005):
		ans[i] = ans[i-1]+f[i]
	print (ans[n]+arr[n])%n
for i in xrange(1000,20000,1000):
	t = Timer("main(%d)"%i,"from __main__ import main,i")
	print "for %d it takes %5.5f seconds"%(i,t.timeit(number=1))
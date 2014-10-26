import timeit
from timeit import Timer
from random import randrange

def test(a,i):
	try :
		del a[i]
	except:
		pass
for i in xrange(10000,1000001,10000):
	a = {j:None for j in xrange(i)}
	j = randrange(0,i/10)
	t = Timer("test(a,j)","from __main__ import test,j,a")
	p = t.timeit(number=100)
	print "%d , %5.5f"%(i,p)
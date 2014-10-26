from matplotlib import pyplot
import sys
from timeit import Timer
import timeit
'''data['format'] = format
data['bytes'] = base64.encodestring(bytes)
sys.stdout.write(image.start)
sys.stdout.write(json.dumps(data))
sys.stdout.write(image_end)
'''
def plot(*a, **k):
	pyplot.plot(*a,**k)

def naive(a,b):
	x = a; y=b
	z = 0
	while x > 0:
	     z = z +y
	     x = x -1
	return z

maxsize = 24
l = 1
ns = [l<<i  for i in range(maxsize)]

#import from main on online IDE but from _main_on a new installation
times1 = [Timer('naive(%d, %d)' %(n, n), 'from __main__ import naive').timeit(number=1) for n in ns]
plot(ns, times1)
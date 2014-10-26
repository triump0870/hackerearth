import time
import resource
def pythongorean_triplet(n):
	start = time.clock()
	count = 0
	for i in range(1,n+1):
		for j in range(i+1,n+1):
			for z in range(j+1,n+1):
				sum = i**2 + j**2
				if sum == z**2:
					print i,j,z
					count +=1
	
	print count
	elp = time.clock() -start
	print "%10.7f seconds"%elp
t = input()
for i in range(t):
	n = input()
	pythongorean_triplet(n)
	
	print resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
n = input()
array = map(int,raw_input().split())
q = input()
for i in xrange(q):
	count = {j:0 for j in array}
	n,m,x = map(int,raw_input().split())
	l,r = n-1,m-1
	index = l
	while l<=r:
		s= array[l] ^ x
		array2 = array[index:r+1]
		if all(s < i for i in array2):
			count[array[l]] += 1


		l += 1
	Z =  max(count,key=count.get)
	print Z,count[Z]
	print '\n'
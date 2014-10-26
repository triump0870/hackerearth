import itertools as it
t = input()
while(t>0):
	t -= 1
	a,d = map(int,raw_input().split())
	A = a if 0<=a<=10**18 else exit(1)
	D = d if 0<=d<=10**18 else exit(1)
	p = input()
	P = p if 1<=p<=10**9 else exit(1)
	array = []
	sum = 0
	for i in it.count(0,1):
		temp = a+i*d
		array.append(temp)
		try:
			if array[i]%p==0:
				print i 
				break
		except:
			print '-1'
	
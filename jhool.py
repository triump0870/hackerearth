tc = int(raw_input())
while(tc>0):
	tc = tc - 1
	n = input()
	b,g = sorted(map(int,raw_input().split()))
	print b,g
	if g-1>b:
		print "jhool"
	else:
		print "teacher"

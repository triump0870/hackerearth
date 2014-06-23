def error():
	exit(1)
l = input()
n = input()
L = l if 1<=l<=10000 else exit(1)
N = n if 1<=n<=1000 else exit(1)
for i in range(N):
	w,h = raw_input().split()
	W = int(w) if 1<=int(w)<=10000 else error()
	H = int(h) if 1<=int(h)<=10000 else error()
	if W<L or H<L:
		print 'UPLOAD ANOTHER'
	else:
		if W*H==L*L:
			print 'ACCEPTED'
		else:
			print 'CROP IT'
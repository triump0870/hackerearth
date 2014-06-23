t = input()
T = t if 1<=t<=1000 else exit(1)
for i in range(T):
	n = input()
	N = n if 1<=n<=10**6 else exit(1)
	dick = {}
	for j in range(1,N+1):
		s,r = raw_input().split()
		S = int(s) if 1<=int(s)<=10**6 else exit(1)
		R = int(r) if 0<=int(r)<=1 else exit(1)
		new = {S:R}
		dick[j]=new
	dick2 = {}
	for k,v in dick.items():
		if 1 in v.values():
			dick2.update(v)
	dickset = {}
	dickset.update(v)
	print dickset
	print len(dick2)
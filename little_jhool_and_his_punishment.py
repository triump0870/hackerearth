import random
import re
jhol = []
bboy = []
ggirl = []
def count_pair(N,jhol):
	global bboy,ggirl
	boy = bboy[:]
	girl = ggirl[:]
	if jhol[0]=='b':
		boy.pop(0)
	else:
		girl.pop(0)
	for c in xrange(1,N):
		if c%2==0:
			if jhol[c-1] == 'b':
				if len(boy)>0:
					jhol.append(boy[0])
					boy.pop(0)
				else:
					jhol.append(girl[0])
					girl.pop(0)
			else:
				if len(girl)>0:
					jhol.append(girl[0])
					girl.pop(0)
				else:
					jhol.append(boy[0])
					boy.pop(0)
		else:
			if jhol[c-1] == 'b' :
				if len(girl)>0:
					jhol.append(girl[0])
					girl.pop(0)
				else:
					jhol.append(boy[0])
					boy.pop(0)
			else:
				if len(boy)>0:
					jhol.append(boy[0])
					boy.pop(0)
				else:
					jhol.append(girl[0])
					girl.pop(0)
	count = 0
	ct = 0
	for x in xrange(len(jhol)-1):
		if jhol[x] == jhol[x+1]:
			count +=1
		else:
			ct += 1
	del jhol[:]
	return count,ct
	
def main():
	global jhol,bboy,ggirl
	t  = input()
	T = t if 1<=t<=50 else exit(1)
	for i in xrange(T):
		n = input()
		N = n if 2<=n<=100 else exit(1)
		b,g = map(int,raw_input().split())
		B= b if 1<=b<=100 else exit(1)
		G = g  if 1<=g<=100 else exit(1)
		if N == (B+G):
			for k in xrange(B):
				bboy.append('b')
			for l in xrange(G):
				ggirl.append('g')
			boy = bboy[:]
			girl = ggirl[:]
			f = Jhool(N,boy)
			s = Jhool(N,girl)
			if f[0]>f[1] or s[0]>s[1]:
				print 'Little Jhool wins!'
			else:
				print 'The teacher wins!'
		else:
			exit(1)
	
def Jhool(N,s):
	global jhol
	temp = s.pop()
	jhol.append(temp)
	return list(count_pair(N,jhol))


if __name__=="__main__":
	main()
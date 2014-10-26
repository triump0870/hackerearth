n = input()
char = []
for i in xrange(n):
	a,b = raw_input().split()
	char.append(a)
	char.append(b)
code = list(raw_input())
for i in xrange(n):
	x= code.index(char[i])
	y= code.index(char[i+1])
	code[x],code[y]=code[y],code[x]
print ''.join(code)

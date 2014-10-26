#!/usr/bin/env python
t = input()
for i in xrange(t):
	a = input()
	a = a % 6
	array = []
	while a >0:
		a = a-1
		array.append(a+1)
		if a==0:
			break
		if a >=2:
			a = a-2
			array.append(a+2)
		if a==0:
			break
		if a >=3:
			a = a-3
			array.append(a+3)
	if len(array) == 0 and a==0:
		print '3'
	else:
		print array[-1]
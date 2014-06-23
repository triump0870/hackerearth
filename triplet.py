n = input()
a = []
for i in range(1,n+1):
	a.append(i*i)
print a
l = (len(a)+1)/2
print l
count = 0
for i in xrange(1,l+1):
	j = i+1
	k = j+1
	while k<len(a)-1 :
		while a[k]<a[i]+a[j]:
			print "pre k=",k
			k +=1
			print "k=",k,'\n'
		if a[k]==a[i]+a[j]:
			count +=1
			print "count=",count,'\n'
		print "last a[k]={0} last a[j]={1} last a[i]={2}".format(a[k],a[j],a[i])
		j +=1

print count
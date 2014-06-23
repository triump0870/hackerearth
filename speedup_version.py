def pythongorean_triplet(n):
	count = 0
	for i in range(1,n+1/2):
		j = i+1
		k = j+1
		while k <= n:
			while k**2 < i**2 + j**2:
				k += 1
			if k**2 == i**2 + j**2:
				count +=1
			j += 1
	return count

def is_range(n,low,up):
    return n if low<=n<=up else exit(1)

t = input()
t = is_range(t,1,100)
for i in range(t):
	n = input()
	n = is_range(n,1,10**6)
	print pythongorean_triplet(n)
t = input()
T = t if 1<=t<=100 else exit(1)
for i in range(T):
	string = list(raw_input())
	alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
	dick = dict(zip(alpha,num))
	if 1<=len(string)<=100:
		j=0
		output = []
		initial  = 0
		while(j<len(string)):
			current = dick.get(string[j])
			dis1 = (current - initial)%26
			dis2 = (initial - current)%26
			if dis1 <= dis2:
				distance = dis1
			else:
				distance = -dis2
			initial = current
			output.append(distance)
			j += 1
		print ','.join(map(str,output))
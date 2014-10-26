from math import ceil
n,m,k = map(int,raw_input().split())
team_cord=[]
check_cord = []
team = []
for i in xrange(n):
	x,y = map(int,raw_input().split())
	team_cord.append((x,y))
for i in xrange(m):
	x,y = map(int,raw_input().split())
	check_cord.append((x,y))
speed=map(int,raw_input().split())
check = []
for i in xrange(n):
	s = []
	for j in xrange(m):
		temp = ceil(((check_cord[j][0]-team_cord[i][0])**2 + (check_cord[j][1]-team_cord[i][1])**2)/float(speed[i])**2)
		team.append(temp)
result = []
for i in xrange(len(team)):
	check = [team[i] for i in team]
import datetime
t = input() 
for i in xrange(t):
	date,month,year = raw_input().split()
	theday = datetime.datetime.strptime('{0} {1} {2}'.format(date,month,year),"%d %B %Y")
	prevday = theday - datetime.timedelta(days=1)
	print prevday.strftime("{0} %B %Y".format(str(prevday.day)))
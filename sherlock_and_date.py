from dateutil.relativedelta import *
import datetime
a = {1:'January',2:'Fabruary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
date,month,year = raw_input().split()
theday = datetime.datetime.strptime('{0} {1} {2}'.format(date,month,year),"%d %B %Y")
prevday = theday + relativedelta(days=-1)
print prevday.day,a[prevday.month],prevday.year
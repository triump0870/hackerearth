t = input()
for i in xrange(t):
	s = raw_input()
	l = str(len(s))
	vol = ['a','e','i','o','u']
	mod = s.lstrip('www.').rstrip('.com')
	for char in vol:
		if char in mod:
			mod = mod.replace(char,'')
	zed = mod+'.com'
	m = str(len(zed))
	print m+'/'+l
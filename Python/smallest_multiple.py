def small(x):
	n = x
	while True:
		for i in xrange(2,x+1):
			if n%i != 0:
				n += 10
				break
		else:
			return n

print small(20)








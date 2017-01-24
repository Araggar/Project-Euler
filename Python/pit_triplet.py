import math

def triplet():	
	for a in xrange(1, 1001):
		for b in xrange(1, 1001):
			c = 1000 - a - b
			if c>0 and math.pow(a,2) + math.pow(b,2) == math.pow(c,2):
				return a*b*c
				
print triplet()
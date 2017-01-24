import math

def prime(x):
	for i in xrange(2,int(math.sqrt(x))+1):
		if x%i==0:
			return False
	return True

x = 1
test_number = 600851475143 
max_num = test_number
while x<=int(math.sqrt(test_number)):
	if prime(x) and test_number%x == 0:
		max_num = x
	x += 1
	
print max_num
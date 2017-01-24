def prime(x):
	counter = 0
	primes = []
	num = 2
	while counter < x:
		for prime in primes:
			if num%prime == 0:
				break
		else:
			primes.append(num)
			counter += 1
		num += 1
	return primes[-1]
	

print prime(10001)		
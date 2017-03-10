def prime(x):
	bitarray = [True]*(x+1)
	p = 2
	while p < x:
			if bitarray[p] == False:
				p = p+1
			else:
				yield p
				i = p + p
				while i <= x:					
					bitarray[i] = False
					i = i + p
				p = p + 1

print sum(prime(2000000))
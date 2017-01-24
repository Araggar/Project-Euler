def fibo(x):
	ante = 0
	post = 1
	yield 0
	while post < x:
		yield post
		ante, post = post,  ante + post
		

print sum([i for i in fibo(4000000) if i%2==0])

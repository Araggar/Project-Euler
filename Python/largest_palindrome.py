def check(x):
	return str(x) == str(x)[::-1]
	
x = 999
y = 999
largest = 0

while (x, y) != (0, 0):
	number = x * y
	if check(number):
		largest = max(number, largest)
	if y == 0:
		x, y = x-1, x	
	else:
		y = y - 1
		
print largest
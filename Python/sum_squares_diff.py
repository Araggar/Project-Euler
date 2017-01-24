import math

sum_square = sum((math.pow(i,2) for i in xrange(101)))
square_sum = math.pow(sum(xrange(101)),2)

print square_sum - sum_square
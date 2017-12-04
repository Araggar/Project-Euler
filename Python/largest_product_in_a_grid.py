#Largest product in a grid


with open("grid_11.txt", 'r') as file:
	grid = file.read().split(' ')

s = 20
largest = 0

grid = list(map(int, grid))

for i in range(20*20 - 63):
	if (i+63)%20 > i%20:
		largest = max(grid[i]*grid[i+21]*grid[i+42]*grid[i+63], largest)

for i in range(20*20 - 60):
	if (i+57)%20 < i%20:
		largest = max(grid[i]*grid[i+19]*grid[i+38]*grid[i+57], largest)

for i in range(20*20 - 3):
	if (i+3)%20 > i%20:
		largest = max(grid[i]*grid[i+1]*grid[i+2]*grid[i+3], largest)

for i in range(20*20 - 60):
	if (i+60)%20 > i%20:
		largest = max(grid[i]*grid[i+20]*grid[i+40]*grid[i+60], largest)

print(largest)


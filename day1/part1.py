# Part 1
with open("measures.txt",'r') as f:

	lines = f.readlines()

increase = 0
for i in range(len(lines)):
	if i - 1 < 0:
		print('(N/A - no previous measurement)')
	else:
		if int(lines[i]) > int(lines[i-1]):
				print('Increase')
				increase = increase + 1
		else:
				print('Decrease')

print(f'Total of {increase} records are increase')






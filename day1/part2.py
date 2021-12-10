#Part II
with open("measures.txt",'r') as f:

	lines = f.readlines()

max_value = max([i for i in range(len(lines)) if  i % 3 == 0])
alp = list(map(chr, range(97,105)))

added = []
char = []
increment = 0

for i in range(max_value):
	suma = 0
	for x in range(3):
			suma = suma + int(lines[i+x])
	char.append(alp[increment] + ":")
	added.append(suma)
	increment += 1
	if increment > 7:
		increment = 0

increase = 0
status = []
for i in range(len(added)):
	if i - 1 < 0:
		status.append('(N/A - no previous sum)')
	else:
		if int(added[i]) > int(added[i-1]):
				status.append('(Increase)')
				increase = increase + 1
		else:
				if int(added[i]) == int(added[i-1]):
					status.append('(No changed)')
				else:
					status.append('(Decrease)')

result = list(zip(char,added, status))

for i in result:
	for x in i:
		print(x, end=' ')
	print('')

print(f'The Increases are {increase}.')




with	open('movements.txt', 'r') as file:
	lines =  file.readlines()

h_position = 0
depth = 0
for i in lines:
	mov = i.split()[0]
	val = int(i.split()[1])

	if mov == 'forward':
		h_position = h_position + val
	elif mov == 'up':
		depth = depth - val
	else:
		depth = depth + val

print(h_position* depth)
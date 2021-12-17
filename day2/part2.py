with	open('movements.txt', 'r') as file:
	lines =  file.readlines()


h_position = 0
depth = 0
aim = 0

for i in lines:
	mov = i.split()[0]
	val = int(i.split()[1])

	if mov == 'down':
		aim = aim + val
	elif mov == 'up':
		aim = aim - val
	else:
		h_position = h_position + val
		depth = depth + (aim * val)


print(h_position*depth)
	
	

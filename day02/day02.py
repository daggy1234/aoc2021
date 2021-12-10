
def p1(cords):
	start_pos = [0,0]

	for cord in cords:
		if cord[0] == 'forward':
			start_pos[0] += cord[1]
		elif cord[0] == 'up':
			start_pos[1] -= cord[1]
		elif cord[0] == 'down':
			start_pos[1] += cord[1]
		else:
			raise Exception(cord[0])
	print(start_pos[0] * start_pos[1])

def p2(cords):
	start_pos = [0,0,0]

	for cord in cords:
		if cord[0] == 'forward':
			start_pos[0] += cord[1]
			start_pos[1] += start_pos[2] * cord[1]
		elif cord[0] == 'up':
			start_pos[2] -= cord[1]
		elif cord[0] == 'down':
			start_pos[2] += cord[1]
		else:
			raise Exception(cord[0])
	print(start_pos[0] * start_pos[1])

if __name__ == '__main__':
	cords = [(lines.split(' ')[0], int(lines.split(' ')[1])) for lines in open("data.txt").readlines()]
	print("Part 1:")
	p1(cords)
	print("Part 2:")
	p2(cords)
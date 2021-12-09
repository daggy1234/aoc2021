def pt1(o):
	lines = []
	cords = []
	for j in range(len(o)):
		for i in range(len(o[j])):
			elm = o[j][i]
			lesserthanright = False
			try:
				lr = o[j][i + 1]
			except IndexError:
				lesserthanright = True
			else:
				if elm < lr:
					lesserthanright = True
			if lesserthanright:
				lesserthanleft = False
				try:
					ll = o[j][i - 1]
					if (i - 1) < 0:
						raise IndexError('a')
				except IndexError:
					lesserthanleft = True
				else:
					if elm < ll:
						lesserthanleft = True
				if lesserthanleft:
					lesserthantop = False
					try:
						lt = o[j - 1][i]
						if (j - 1) < 0:
							raise IndexError('a')
					except IndexError:
						lesserthantop = True
					else:
						if elm < lt:
							lesserthantop = True
					if lesserthantop:
						lesserthanbot = False
						try:
							lt = o[j + 1][i]
						except:
							lesserthanbot = True
						else:
							if elm < lt:
								lesserthanbot = True
						if lesserthanbot:
							lines.append(elm)
							cords.append((j,i))

	print(len(lines) + sum(lines))
	return cords

def compute_basins(inp, visited_nodes, o):
	if inp in visited_nodes:
		return []
	else:
		visited_nodes.append(inp)
	left_cords = []
	i_v = inp[1]
	j_v = inp [0]
	new_bto_iv = i_v
	while True:
		new_bto_iv -=  1
		if (new_bto_iv) < 0:
			break
		new_elm = o[j_v][new_bto_iv]
		if new_elm != 9:
			left_cords.append((j_v, new_bto_iv))
		else:
			break
	right_cords = []
	new_bto_il = i_v
	while True:
		new_bto_il +=  1
		if (new_bto_il) >= len(o[0]):
			break
		new_elm = o[j_v][new_bto_il]
		if new_elm != 9:
			right_cords.append((j_v, new_bto_il))
		else:
			break
	top_cords = []
	new_bto_jv = j_v
	while True:
		new_bto_jv -=  1
		if (new_bto_jv) < 0:
			break
		new_elm = o[new_bto_jv][i_v]
		if new_elm != 9:
			top_cords.append((new_bto_jv, i_v))
		else:
			break
	bot_cords = []
	new_bto_jb = j_v
	while True:
		new_bto_jb +=  1
		if (new_bto_jb) >= len(o):
			break
		new_elm = o[new_bto_jb][i_v]
		if new_elm != 9:
			bot_cords.append((new_bto_jb, i_v))
		else:
			break
	basin_cords = left_cords + right_cords + top_cords + bot_cords
	for cord in basin_cords:
		basin_cords += compute_basins(cord, visited_nodes, o)
	return list(set(basin_cords))



def pt2(cords, o):
	basin_sizes = []
	visited_nodes = []
	for cord in cords:
		basin_sizes.append(len(compute_basins(cord, visited_nodes, o)))
		print(basin_sizes)
	basin_sizes.sort(reverse=True)
	print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])

if __name__ == "__main__":
	o = [[int(char) for char in line.strip()] for line in open("data.txt").readlines()]
	print(f"Part 1:")
	cords = pt1(o)
	print("Part 2:")
	pt2(cords, o)
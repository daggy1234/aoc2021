from collections import Counter
from typing import  List, Tuple

POINT = Tuple[int, int]

POINT_PAIR = List[POINT]

POINT_VEC = List[POINT_PAIR]



def parse_cords() -> Tuple[POINT_VEC, POINT_VEC, POINT_VEC]:
	parsed = [[f.split(",") for f in line.replace('\n',"").split(" -> ")] for line in open("data.txt").readlines()]
	misc = []
	filtered_y = []
	filtered_x = []
	for cord in parsed:
		if cord[0][0] == cord[1][0]:
			filtered_y.append(cord)
		elif cord[0][1] == cord[1][1]:
			filtered_x.append(cord)
		else:
			misc.append(cord)
	return misc, filtered_x, filtered_y

def compute_horizontal(filtered_y: POINT_VEC) -> List[POINT]:
	all_cds = []
	for cordy in filtered_y:
		cord_y_a = int(cordy[0][1])
		cord_y_b = int(cordy[1][1])
		cord_x = int(cordy[0][0])
		if cord_y_a > cord_y_b:
			temp = cord_y_a
			cord_y_a = cord_y_b
			cord_y_b = temp
		for fcord in list(range(cord_y_a,cord_y_b + 1)):
			all_cds.append((cord_x, fcord))
	return all_cds

def compute_vertical(filtered_x: POINT_VEC) -> List[POINT]:
	all_cds = []	
	for cordy in filtered_x:
		cord_x_a = int(cordy[0][0])
		cord_x_b = int(cordy[1][0])
		cord_y = int(cordy[0][1])
		if cord_x_a > cord_x_b:
			temp = cord_x_a
			cord_x_a = cord_x_b
			cord_x_b = temp
		for fcord in list(range(cord_x_a,cord_x_b + 1)):
			all_cds.append((fcord, cord_y))
	return all_cds
def compute_diagonals(misc: POINT_VEC) -> List[POINT]:
	c_l_g = []
	for cord in misc:
		cord_x_a = int(cord[0][0])
		cord_x_b = int(cord[1][0])
		cord_y_a = int(cord[0][1])
		cord_y_b = int(cord[1][1])
		grad = (cord_y_b - cord_y_a) // (cord_x_b - cord_x_a)
		if grad > 0:
			if cord_y_a > cord_y_b:
				temp_y = cord_y_a
				cord_y_a = cord_y_b
				cord_y_b = temp_y
				temp_x = cord_x_a
				cord_x_a = cord_x_b
				cord_x_b = temp_x
			c_l = [(cord_x_a, cord_y_a)]
			cter = 1
			while True:
				new_cd_x = cord_x_a + cter
				new_cd_y = cord_y_a + cter
				if (new_cd_x >= cord_x_b) or (new_cd_y >= cord_y_b):
					break
				c_l.append((new_cd_x, new_cd_y))
				cter += 1
			c_l.append((cord_x_b, cord_y_b))
		else:
			if cord_y_b > cord_y_a:
				temp_y = cord_y_a
				cord_y_a = cord_y_b
				cord_y_b = temp_y
				temp_x = cord_x_a
				cord_x_a = cord_x_b
				cord_x_b = temp_x
			c_l = [(cord_x_a, cord_y_a)]
			cter = 1
			while True:
				new_cd_x = cord_x_a + cter
				new_cd_y = cord_y_a - cter
				if (new_cd_x >= cord_x_b) or (new_cd_y <= cord_y_b):
					break
				c_l.append((new_cd_x, new_cd_y))
				cter += 1
			c_l.append((cord_x_b, cord_y_b))
		c_l_g += c_l
	return c_l_g

def with_grid():
	max_grid_a = [[0 for j in range(1000)] for i in range(1000)]
	misc, filt_x, filt_y = parse_cords()
	all_cds = []
	all_cds += compute_horizontal(filt_y)
	all_cds += compute_vertical(filt_x)
	print("Part 1:")
	for cd in all_cds:
		max_grid_a[cd[1]][cd[0]] += 1
	c_g_t = 0
	for row in max_grid_a:
		for col in row:
			if col >= 2:
				c_g_t += 1
	print(c_g_t)
	print("Part 2:")
	max_grid_b = [[0 for j in range(1000)] for i in range(1000)]
	all_cds += compute_diagonals(misc)
	for cd in all_cds:
		max_grid_b[cd[1]][cd[0]] += 1
	c_g_t = 0
	for row in max_grid_b:
		for col in row:
			if col >= 2:
				c_g_t += 1
	print(c_g_t)

def with_dict():
	misc, filt_x, filt_y = parse_cords()
	all_cds = []
	all_cds += compute_horizontal(filt_y)
	all_cds += compute_vertical(filt_x)
	print("Part 1:")
	print(sum(cord_occ >= 2 for cord_occ in Counter(all_cds).values()))
	print("Part 2:")
	all_cds += compute_diagonals(misc)
	print(sum(cord_occ >= 2 for cord_occ in Counter(all_cds).values()))

if __name__ == '__main__':
	print("WITH GRID!")
	with_grid()
	print("WITH DICT!")
	with_dict()




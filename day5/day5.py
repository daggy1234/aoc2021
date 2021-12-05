


max_grid = [[0 for j in range(1000)] for i in range(1000)]

parsed = [[f.split(",") for f in line.replace('\n',"").split(" -> ")] for line in open("data.txt").readlines()]
filtered_y = []
filtered_x = []
misc = []

for cord in parsed:
	if cord[0][0] == cord[1][0]:
		filtered_y.append(cord)
	elif cord[0][1] == cord[1][1]:
		filtered_x.append(cord)
	else:
		misc.append(cord)

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
misx_cd_a = []
misx_cd_b = []
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
	all_cds += c_l

for cd in all_cds:
	max_grid[cd[1]][cd[0]] += 1

print(max_grid)

c_g_t = 0
for row in max_grid:
	for col in row:
		if col >= 2:
			c_g_t += 1
print(c_g_t)
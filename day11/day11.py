from typing import Set, Tuple

def print_grid(inp):
	print("=" * 10)
	rows = []
	for j in range(max_s):
		row = ""
		for i in range(max_s):
			if len(str(inp[(j,i)])) > 1:
				row += f"({(inp[(j,i)])})"
			else:
				row += str(inp[(j,i)])
		rows.append(row)
	print('\n'.join(rows))
	return '\n'.join(rows)
			


def burst(cord: Tuple[int,int],vcords: Set[Tuple[int,int]] ,ninib: bool = False):
	cdic[cord] += 1
	if cord in vcords:
		return vcords
	outv = cdic[cord]
	if outv > 9:
		vcords.add(cord)
		cord_ops = [
			(0,-1), (0,1),(1,0), (-1,0),
			(-1,-1), (1,1), (-1,1), (1,-1)
		]
		for op in cord_ops:
			y_v = cord[0] + op[0]
			x_v = cord[1] + op[1]
			if (0 <= x_v < max_s) and (0 <= y_v < max_s):
				burst((y_v, x_v),vcords)
	return vcords

def pt1(cdic):
	burtc = 0
	for i in range(100):	
		vcords = set()
		for k in cdic.keys():
			cdic[k] += 1
		for k in cdic.keys():
			if cdic[k] > 9:
				vcords = burst(k,vcords,True)
		for k in cdic.keys():
			if cdic[k] > 9:
				burtc += 1
				cdic[k] = 0
	print_grid(cdic)

def pt2(cdic):
	turns = 0
	while True:
		turns += 1
		vcords = set()
		for k in cdic.keys():
			cdic[k] += 1
		for k in cdic.keys():
			if cdic[k] > 9:
				vcords = burst(k,vcords,True)
		for k in cdic.keys():
			if cdic[k] > 9:
				cdic[k] = 0
		if all([v == 0 for v in cdic.values()]):
			print("pog")
			break
	return 100 + turns

if __name__ == '__main__':
	parsed = [[int(v) for v in line.strip()] for line in open("data.txt").readlines()]
	cdic = {}
	max_s = len(parsed[0])
	for j,jv in enumerate(parsed):
		for i,iv in enumerate(jv):
			cdic[(j,i)] = iv
	pt1(cdic)
	print(pt2(cdic))
from typing import Tuple
from functools import lru_cache
import math

ta = "target area: x=175..227, y=-134..-79"
# ta = "target area: x=240..292, y=-90..-57"

cds = [[int(e) for e in v[2:].split("..")] for v in ta.split(": ")[1].split(", ")]

@lru_cache()
def compute_t(iv,jv) -> Tuple[int, bool]:
	start_loc = [0,0]
	max_y = -999999
	while (not ((cds[0][0] <= start_loc[0] <= cds[0][1]) and (cds[1][0] <= start_loc[1] <= cds[1][1]))):
		start_loc[0] += iv
		start_loc[1] += jv
		if iv > 0:
			iv -= 1
		elif iv < 0:
			iv += 1
		jv -= 1
		if start_loc[1] >= max_y:
			max_y = start_loc[1]

		if (iv > cds[0][1]) or  (jv < cds[1][0]):
			return 0,False
	return max_y,True

# def cmh(iv,jv):
# 	v = ((iv ** 2) + (jv ** 2))
# 	st = (iv / jv) ** 2
# 	print((v * st) / 2)




vvs = []
maxs = []
for i in range(-1000,1000):
	for j in range(-1000,1000):
		out,s = compute_t(i,j)
		if s:
			maxs.append(abs(out))
print(max(maxs))
print(len(maxs))


# (1225, (20, 49))

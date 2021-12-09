from typing import List

def p1(hor_pos: List[int]):
	fuel_dict = {}
	for val in range(min(hor_pos), max(hor_pos)):
		if not fuel_dict.get(val):
			for subv in hor_pos:
				try:
					fuel_dict[val] += abs(subv - val)
				except KeyError:
					fuel_dict[val] = abs(subv - val)
	print(min(fuel_dict.values()))

def compute_fuel(base: int, dest: int) -> int:
	s_v = 1
	nc = 0
	fc = 0
	diff = abs(base - dest) - 1
	while nc <= diff:
		fc += s_v
		s_v += 1
		nc += 1
	return fc

def p2_slow(hor_pos: List[int]):
	fuel_dict = {}
	for val in range(min(hor_pos), max(hor_pos)):
		if not fuel_dict.get(val):
			for subv in hor_pos:
				try:
					fuel_dict[val] += compute_fuel(val, subv)
				except KeyError:
					fuel_dict[val] = compute_fuel(val, subv)
	print(min(fuel_dict.values()))

def p2_fast(hor_pos: List[int]):
	fuel_dict = {}
	for val in range(min(hor_pos), max(hor_pos)):
		if not fuel_dict.get(val):
			for subv in hor_pos:
				try:
					fuel_dict[val] += sum(range(0, abs(val - subv) + 1))
				except KeyError:
					fuel_dict[val] = sum(range(0, abs(val - subv) + 1))
	print(min(fuel_dict.values()))

def p2_fastest(hor_pos: List[int]):
	fuel_dict = {}
	for val in range(min(hor_pos), max(hor_pos)):
		if not fuel_dict.get(val):
			fuel_dict[val] = sum([sum(range(0, abs(val - subv) + 1)) for subv in hor_pos])
	print(min(fuel_dict.values()))

def p2_godtier(hor_pos: List[int]):
	fuel_dict = {}
	for val in range(min(hor_pos), max(hor_pos)):
		if not fuel_dict.get(val):
			fuel_dict[val] = sum([[absol := abs(val - subv), (absol * (absol + 1)) // 2][1] for subv in hor_pos])
	print(min(fuel_dict.values()))

if __name__ == '__main__':
	hor_pos = [int(v) for v in open('data.txt').readline().split(",")]
	p1(hor_pos)
	p2_godtier(hor_pos)
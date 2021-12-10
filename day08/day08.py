import itertools
from typing import List, Set

def pt1(outputts):
	ct = 0
	for v in outputts:
		for subs in v.split(' '):
			print(subs)
			print(len(subs))
			if len(subs) in [2,4,7,3]:
				ct += 1
	print(ct)


len_d = {
	2: 1,
	3: 7,
	4: 4,
	7: 8
}


stan_d = {
	1: "ab",
	2: "gcdfa",
	3: "fbcad",
	4: "eafb",
	5: "cdfbe",
	6: "cdfgeb",
	7: "dab",
	8: "acedgfb",
	9: "cefabd",
}

pixel_array = [0,0,0,0,0,0,0]


def compute_occurance_set(v: str, keyv, mapping):
	
	num_one_f = 0
	ourpix = pixrays[keyv]
	for char in v:
		try:
			num_one_f = ourpix.index(1, num_one_f)
		except ValueError:
			continue
		else:
			try:
				mapping[char].append(num_one_f)
			except KeyError:
				mapping[char] = [num_one_f]
			num_one_f += 1
	return mapping




def p2(outputts):
	key_str = outputts[0].split(' ')
	mapping = {}
	non_unique = {}
	for v in key_str:
		if keyv := len_d.get(len(v)):
			mapping[keyv] = set(v)
		else:
			try:
				non_unique[len(v)].append(set(v))
			except KeyError:
				non_unique[len(v)] = [set(v)]
	for setv in non_unique[6]:
		if len(setv.intersection(mapping[1])) == 1:
			mapping[6] = setv
		elif len(setv.intersection(mapping[4])) == 4:
			mapping[9] = setv
		else:
			mapping[0] = setv
	for setv in non_unique[5]:
		if len(setv.intersection(mapping[1])) == 2:
			mapping[3] = setv
		elif len(setv.intersection(mapping[4])) == 2:
			mapping[2] = setv
		else:
			mapping[5]= setv
	to_decode_str = [set(v) for v in outputts[1].split(' ')]
	inp_s = ""
	for todec in to_decode_str:
		f = False
		for k,v in mapping.items():
			if todec == v:
				inp_s += str(k)
				f = True
				break
	return inp_s


def pt2(outputts):
	tsum = 0
	for i,o in enumerate(outputts):
		tsum += int(p2(o))
	print(tsum)

if __name__ == '__main__':
	outputts = [[subv.strip() for subv in v.split("|")] for v in open("data.txt").readlines()]
	print("Part 1:")
	pt1(outputts)
	print("Part 2:")
	pt2(outputts)

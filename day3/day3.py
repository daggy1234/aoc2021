from collections import Counter

data = [val.replace('\n', '') for val in open("data.txt").readlines()]

def part_a():
	cd = {}
	for val in data:
		for i,v in enumerate(val):
			try:
				cd[i].append(v)
			except KeyError:
				cd[i] = [v]
	print(cd)

	new_cd = {}
	less_cd = {}
	for k,v in cd.items():
		mc = Counter(v).most_common()
		new_cd[k] = mc[0][0]
		less_cd[k] = mc[1][0]
	print(new_cd)
	print(less_cd)

	len_s = len(data[0])
	print(len_s)
	max_str = ""
	less_str = ""
	for i in range(len_s):
		max_str += new_cd[i]
		less_str += less_cd[i]

	gamma = int(max_str, base=2)
	expsilon = int(less_str, base=2)

	print(gamma * expsilon)


def part_b():
	mc_data = data
	lc_data = data
	mcb_g = None
	lcb_g = None
	mcb_f = False
	lcb_f = False
	len_s = len(data[0])
	for i in range(len_s):
		print(f"i = {i}")
		mc = Counter([val[i] for val in mc_data]).most_common()
		mcb = mc[0][0]
		if not mcb_f:
			if mc[0][1] == mc[1][1]:
				mcb = '1'
		mc_data = [val for val in mc_data if val[i] == mcb]
		if len(mc_data) == 1 and mcb_f == False:
			mcb_g = mc_data
			mcb_f = True
		if mcb_f:
			break
		print(mc_data)

	for i in range(len_s):
		print(f"i = {i}")
		lc = Counter([val[i] for val in lc_data]).most_common()
		try:
			lcb = lc[1][0]
		except IndexError:
			lcb = lc[0][0]
		if not lcb_f:
			if lc[0][1] == lc[1][1]:
				lcb = '0'
		lc_data = [val for val in lc_data if val[i] == lcb]
		print(len(lc_data) == 1 and lcb_f == False)
		if len(lc_data) == 1 and lcb_f == False:
			lcb_g = lc_data
			lcb_f = True
		if lcb_f:
			break
		print(lc_data)


	o = int(mcb_g[0], base=2)
	c = int(lcb_g[0], base=2)
	print(o * c)

if __name__ == '__main__':
	part_a()
	part_b()

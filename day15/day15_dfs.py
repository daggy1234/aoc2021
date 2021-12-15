from typing import List, Tuple




def compute_path_slow(p):
	top_r = (0,0)
	bot_lef = (len(p) - 1, len(p[0]) - 1)
	print(f" Bot Lef {bot_lef}")

	def recur_path(top_r: Tuple[int,int], v: List[Tuple[Tuple[int,int],int]]) -> int:
		ops = [(0,1),(1,0)]
		risk_d = []
		if top_r[0] >= len(p) or top_r[1]  >= len(p[0]):
			return sum([aka[1] for aka in v])
		if top_r == bot_lef:
			return sum([aka[1] for aka in v])
		for op in ops:
			try:
				risk_d.append((p[top_r[0] + op[0]][top_r[1] + op[1]], op, (top_r[0] + op[0],top_r[1] + op[1] )))
			except IndexError:
				continue
		el = []
		for val in risk_d:
			out = recur_path(val[2], v + [(val[2], val[0])])
			if isinstance(out,int):
				el.append(out)
			else:
				el.extend(out)
		return el



	o = recur_path(top_r,[(top_r,p[0][0])])
	f = min(o) - p[0][0]
	print(f)





if __name__ == '__main__':
	print("DO NOT RUN FOR MAIN. This is extremely slow and inefficient.")
	p = [[int(v) for v in o.strip()] for o in open("test_data.txt").readlines()]
	compute_path_slow(p)

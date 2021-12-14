from typing import Counter, Dict, List, Tuple
import time

def parser(file) -> Tuple[str, List[Tuple[str,str]]]:
	l = open(file).readlines()
	base_opt = l[0].strip()
	return base_opt, [tuple(v.strip().split(" -> ")) for v in l[2:]]

def p1(base,inserts, iters):
	for p in range(iters):
		to_inserts = {}
		toincr = 0
		for i in range(len(base) - 1):
			opt = base[i] + base[i + 1]
			opts = [v for v in inserts if v[0] == opt]
			if opts:
				to_inserts[i + 1 + toincr] =  opts[0]
				toincr += 1

		basel = list(base)
		for k,v in to_inserts.items():
			basel.insert(k,v[1])
		base = ''.join(basel)

	c = Counter(list(base)).most_common()
	print(c[0][1] - c[-1][1])


def compute_freq_d(base: str) -> Dict[str, int]:
	freq_d = {}
	for i in range(len(base) - 1):
		opt = base[i] + base[i + 1]
		try:
			freq_d[opt] += 1
		except KeyError:
			freq_d[opt] = 1
	return freq_d

def p2(base,inserts, iters):
	freq_d = compute_freq_d(base)
	for p in range(iters):
		new_fd = {}
		for i in inserts:
			if freq_d.get(i[0]):
				tc = freq_d[i[0]]
				freq_d[i[0]] = 0
				new_ls = list(i[0])
				try:
					new_fd[new_ls[0] + i[1]] += tc
				except KeyError:
					new_fd[new_ls[0] + i[1]] = tc
				try:
					new_fd[i[1] + new_ls[1]] += tc
				except KeyError:
					new_fd[i[1] + new_ls[1]] = tc
		freq_d = new_fd
	letcts = {}
	pairs = [(k,v) for k,v in freq_d.items()]
	for pair in pairs:
		k = pair[0]
		v = pair[1]
		try:
			letcts[k[0]] += v
		except KeyError:
			letcts[k[0]] = v
	letcts[base[-1]] += 1
	out = [v for v in letcts.values()]
	print(max(out) - min(out))

if __name__ == '__main__':
	base, inserts = parser("data.txt")
	print("Part 1:")
	s = time.perf_counter_ns()
	p1(base, inserts, 10)
	e = time.perf_counter_ns()
	print(f"Part 1 Slow: {(e -s)  / (10 ** 6) }")
	s = time.perf_counter_ns()
	p2(base, inserts, 10)
	e = time.perf_counter_ns()
	print(f"Part 1 Fast: {(e -s) / (10 ** 6) }")
	print("Part 2:")
	p2(base,inserts, 40)
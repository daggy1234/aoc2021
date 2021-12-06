from collections import Counter
import contextlib



def p1():
	in_states = [int(v) for v in open("data.txt").readline().split(",")]
	for days in range(18):
		for i,ct in enumerate(in_states):
			if ct == 0:
				in_states.append(9)
				in_states[i] = 6
			else:
				in_states[i] -= 1

	print(len(in_states))

def p2():
	in_states = dict(Counter([int(v) for v in open("data.txt").readline().split(",")]))
	in_states[6] = 0
	in_states[8] = 0
	for days in range(256):
		new_d = {}
		for k,v in in_states.items():
			new_d[k-1] = v
		with contextlib.suppress(KeyError):
			new_c = new_d[-1]
			if new_d.get(6):
				new_d[6] += new_c
			else:
				new_d[6] = new_c
			if new_d.get(8):
				new_d[8] += new_c
			else:
				new_d[8] = new_c
			new_d.pop(-1)
		in_states = new_d
	print(sum(v for v in in_states.values()))

if __name__ == '__main__':
	p1()
	p2()

in_states = [int(v) for v in open("data.txt").readline().split(",")]

for days in range(256):
	for i,ct in enumerate(in_states):
		if ct == 0:
			in_states.append(9)
			in_states[i] = 6
		else:
			in_states[i] -= 1

print(len(in_states))
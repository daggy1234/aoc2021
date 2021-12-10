match_dict = {
	"]": "[",
	")": "(",
	">": "<",
	"}": "{",
}

match_dict_b = {
	 "[": "]",
	 "(": ")",
	 "<": ">",
	 "{": "}",
}


scores = {
    ")": 3,
    "]":  57,
    "}": 1197,
    ">": 25137
}

scores_b = {
    ")": 1,
    "]":  2,
    "}": 3,
    ">": 4
}


pop_errors = []


def topper(stack):	
	try:
		return stack[-1]
	except IndexError:
		return None


def gen_missing(exp):
	stack = []
	for char in exp:
		if char in ["[", "(", "{", "<"]:
			stack.append(char)
		else:
			top = topper(stack)
			while top != match_dict[char]:
				stack.pop()
				top = topper(stack)
			stack.pop()
	matched = [match_dict_b[stack[i]] for i in range(len(stack) - 1,-1,-1)]
	tot = 0
	for v in matched:
		tot = ((tot * 5) + scores_b[v])
	return tot

def process_exp(exp):
	global pop_errors
	stack = []
	corrupt = True
	for char in exp:
		if char in ["[", "(", "{", "<"]:
			stack.append(char)
		else:
			top = topper(stack)
			if top == match_dict[char]:
				stack.pop()
			else:
				pop_errors.append(char)
				corrupt = False
				break
	return corrupt

if __name__ == '__main__':
	inc = [exp.strip() for exp in open("data.txt").readlines() if process_exp(exp.strip())]
	print("Part 1:")
	print(sum([scores[v]  for v in pop_errors]))
	print("Part 2:")
	scores = []
	for val in inc:
		scores.append(gen_missing(val))
	scores.sort()
	print(scores[len(scores) // 2])
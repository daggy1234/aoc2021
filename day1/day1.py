def part_1(parse_data):
	inc_ct = 0
	last_val = parse_data[0]
	for val in parse_data:
		if val > last_val:
			inc_ct +=1 
		last_val = val
	return inc_ct

def saatvik_solution(parse_data):
	count = 0
	for i in range(3, len(parse_data)):
		if parse_data[i] > parse_data[i-3]:
			count += 1
	return count

def arnav_soln(parse_data):
	count = 0
	last_val = parse_data[0]
	for i in range(1, len(parse_data) - 2):
		suma = parse_data[i] + parse_data[i+1] + parse_data[i+2]
		if suma > last_val:
			count += 1
		last_val = suma
	return count


if __name__ == '__main__':
	parse_data = [int(v) for v in open("data.txt").readlines()]
	print(part_1(parse_data))
	print(saatvik_solution(parse_data))
	print(arnav_soln(parse_data))
from typing import List, Tuple
import string




def recur_path_pt1(curr_path: List[str] ,all_paths: List[Tuple[str, str]], small_caves: List[str], small_cave_count: int) -> List[List[str]]:
	for val in small_caves:
		if curr_path.count(val) > 1:
			return []

	final_paths = []
	start = curr_path[-1]
	if start == 'end':
		return [curr_path]
	next_steps = []
	for path in all_paths:
		if path[0] == start:
			next_steps.append(path[1])
	pathways = [curr_path + [step] for step in next_steps]
	for path in pathways:
		out = recur_path_pt1(path, all_paths, small_caves, small_cave_count)
		final_paths.extend(out)
	return [path for path in final_paths if len(path) > 0]


def recur_path_pt2(curr_path: List[str] ,all_paths: List[Tuple[str, str]], small_caves: List[str],once_caves: List[str]) -> List[List[str]]:
	smcc = []
	for val in small_caves:
		pc = curr_path.count(val)
		if  1 < pc < 3 :
			smcc.append(val)
	if len(smcc) > 1:
		return []

	for val in small_caves:
		if val not in smcc and curr_path.count(val) > 1:
			return []

	for val in once_caves:
		if curr_path.count(val) > 1:
			return []

	final_paths = []
	start = curr_path[-1]
	if start == 'end':
		return [curr_path]
	next_steps = []
	for path in all_paths:
		if path[0] == start:
			next_steps.append(path[1])
	pathways = [curr_path + [step] for step in next_steps]
	for path in pathways:
		out = recur_path_pt2(path, all_paths, small_caves,once_caves)
		final_paths.extend(out)
	return [path for path in final_paths if len(path) > 0]

def gen_shortpaths(all_paths: List[Tuple[str, str]]):
	allcps = []
	for v in [val.strip().split('-') for val in open("data.txt").readlines()]:
		allcps.extend([v[0], v[1]])
	allcps = list(set(allcps))
	sortedl = []
	for val in allcps:
		if val[0] not in string.ascii_uppercase:
			sortedl.append(val)
	return sortedl

if __name__ == '__main__':
	paths = [tuple(val.strip().split('-')) for val in open("data.txt").readlines()]
	all_paths = paths + [path[::-1] for path in paths]
	sortedl = gen_shortpaths(all_paths)
	start_end_l = ['start', 'end']
	sortedl_pt2 = [v for v in sortedl if v not in start_end_l]
	print("Part 1:")
	out = recur_path_pt1(['start'], all_paths,sortedl , 0)
	print(len(out))
	print("Part 2:")
	out2 = recur_path_pt2(['start'], all_paths,sortedl_pt2,start_end_l)
	print(len(out2))


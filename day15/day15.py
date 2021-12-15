from typing import Tuple, List
import heapq





class Queue:

	la: List[Tuple[Tuple[int,int], int]]

	def __init__(self) -> None:
		self.la = [((0,0),0)]
	
	def dequeue(self) -> Tuple[int, Tuple[int,int]]:
		o = self.la.pop(0)
		return o

	def enqueue(self, v: Tuple[int, Tuple[int,int]]):
		self.la.append(v)
		self.la.sort(key=lambda x : x[1])

	def __str__(self) -> str:
		return str(self.la)







def djikstracomputelol(graph, queue,sets , end):
	while True:
		o = queue.dequeue()
		if o[0] in sets:
			continue
		sets.add(o[0])
		children = graph[o[0]]
		for child in children:
			if child[0] in sets:
				continue
			elif child[0] == end[0]:
				return child[1] + o[1]
			else:
				queue.enqueue((child[0], child[1] + o[1]))

def djikstracomputeheapq(graph, queue,sets , end):
	while True:
		ore = heapq.heappop(queue)
		o = ore[::-1]
		if o[0] in sets:
			continue
		sets.add(o[0])
		children = graph[o[0]]
		for child in children:
			if child[0] in sets:
				continue
			elif child[0] == end[0]:
				return child[1] + o[1]
			else:
				heapq.heappush(queue,(child[1] + o[1],child[0]))

def make_graph(p):
	graph = {}
	for i,il in enumerate(p):
		for j,jl in enumerate(il):
			ops = [(0,1), (0,-1), (-1,0), (1,0)]
			cords = []
			for op in ops:
				newi,newj = (i + op[0], j + op[1])
				if 0 <= newi < len(p) and 0 <= newj < len(il):
					cords.append(((newi, newj), p[newi][newj]))
			graph[(i,j)] = cords
	return graph

def pt1(p):
	end = ((len(p) - 1, len(p[-1]) - 1), p[-1][-1])
	graph = make_graph(p)
	beentheredonethat = set()
	queue = Queue()
	o = djikstracomputelol(graph, queue, beentheredonethat, end)
	print(o)




def pt2(p,mplier):
	graphp = {}
	for i,il in enumerate(p):
		for ik in range(5):
			for j,jl in enumerate(il):
				for jk in range(mplier):
					pnewi,pnewj = (i + (len(p) * ik), j + (len(il) * jk))
					op =  p[i][j] + jk + ik
					if op > 9:
						op -= 9
					graphp[(pnewi,pnewj)] = op
	lins = []
	for i in range(len(p) * mplier):
		subl = []
		for j in range(len(p[0]) * mplier):
			subl.append(graphp[(i,j)])
		lins.append(subl)
	p = lins
	end = ((len(p) - 1, len(p[-1]) - 1), p[-1][-1])
	graph = make_graph(p)
	beentheredonethat = set()
	queue = []
	heapq.heappush(queue, (0,(0,0)))
	o = djikstracomputeheapq(graph, queue, beentheredonethat, end)
	print(o)

if __name__ == '__main__':
	p = [[int(v) for v in o.strip()] for o in open("data.txt").readlines()]
	print("Part 1:")
	pt1(p)
	print("Part 2:")
	pt2(p,5)


from typing import List, Tuple
from copy import deepcopy

class GameBoard:

    def __init__(self, inp: List[List[int]], gid: int) -> None:
        self.game_board = inp
        self._gid = gid
        self.i_v = len(self.game_board)
        self.j_v = len(self.game_board[0])

    def check_inp_present(self, num: int) -> bool:
        for i in range(self.i_v):
            for j in range(self.j_v):
                if self.game_board[i][j] == num:
                    self.game_board[i][j] = -1
                    return self.winner_check()
        return False

    def summa(self) -> int:
        tot_sum = 0
        for i in range(self.i_v):
            for j in range(self.j_v):
                if self.game_board[i][j] != -1:
                    tot_sum += self.game_board[i][j]
        return tot_sum

    def winner_check(self) -> bool:
        for row in self.game_board:
            if all([v == -1 for v in row]):
              return True
        each_row = []
        for j in range(self.j_v):
            e_v = []
            for i in range(self.i_v):
                e_v.append(self.game_board[i][j])
            if all([v == -1 for v in e_v]):
              return True
        return False

    def g_board_print(self):
        print(self.game_board)

def parse_inputs() -> Tuple[List[int],List[GameBoard]]:
    inp = [line.replace('\n','').replace('  ', ' ').strip() for line in open('data.txt').readlines()] + ['']
    i_pop = inp.pop(0)
    nums = [int(v) for v in i_pop.split(',')]
    inp.pop(0)
    boards = []
    cter = 0
    max_iter = 0
    end_of_list_reached = False
    while cter < len(inp) or end_of_list_reached:
        sub_board = []
        for i in range(cter,len(inp)):
            if inp[i] == '':
                boards.append(sub_board)
                sub_board = []
                cter = i + 1
                max_iter += 1
                break
            else:
                sub_board.append(inp[i])

    return nums, [GameBoard([[int(ca) for ca in v.split(' ')] for v in board], i)  for i,board in enumerate(boards)]

def part_a(nums: List[int], parsed: List[GameBoard]):
    parent_break = False
    for num in nums:
        if parent_break:
            break
        for board in parsed:
            if board.check_inp_present(num):
                parent_break = True
                print(board.summa() * num)
def part_b(nums: List[int], parsed: List[GameBoard]):
    parsed_clone = deepcopy(parsed)
    parent_break = False
    for j,num in enumerate(nums):
        if len(parsed) == 1:
            break
        to_pop = []
        for i,board in enumerate(parsed):
            if board.check_inp_present(num):
                to_pop.append(i)
        parsed = [parsed[i] for i, e in enumerate(parsed) if i not in to_pop]
        print(parsed)
    losing_board = parsed_clone[parsed[0]._gid]
    for num in nums:
        if losing_board.check_inp_present(num):
            print(losing_board.summa() * num)
            break

nums, boards = parse_inputs()
part_b(nums, boards)
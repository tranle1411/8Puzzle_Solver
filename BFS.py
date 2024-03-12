import copy
import helper
from collections import deque


class bfs:
    def __init__(self, n):
        self.n = n
        self.open = deque()
        self.closed = []
        self.expand = 0

    def solve(self):
        n = helper.info(self.n, None)

        while n.arr != helper.getGoal():
            u, v = helper.find_empty(n.arr)
            # generate OPEN
            for i in range(4):
                u_new = u + helper.moves()[i][0]
                v_new = v + helper.moves()[i][1]
                if 0 <= u_new <= 2 and 0 <= v_new <= 2:
                    n_new = helper.info(helper.swapPositions(n.arr, u, v, u_new, v_new), n)
                    i = 0
                    while i < len(self.closed) and n_new.arr != self.closed[i].arr: i += 1
                    if i == len(self.closed):
                        self.expand += 1
                        self.open.append(n_new)
            self.closed.append(n)
            if len(self.open) == 0:
                print("Can't find solution!")
                exit(1)
            else:
                n = self.open.popleft()

        # final moves
        helper.print_final_path(n, self.n, self.expand)

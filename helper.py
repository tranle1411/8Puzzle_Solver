import copy


# goal puzzle
def getGoal():
    goal = [['1', '2', '3'],
            ['8', '0', '4'],
            ['7', '6', '5']]
    return goal


# Swap positions in puzzle
def swapPositions(n, x1, y1, x2, y2):
    n_new = copy.deepcopy(n)
    n_new[x1][y1], n_new[x2][y2] = n[x2][y2], n[x1][y1]
    return n_new


def print_array(arr):
    for i in range(3): print(arr[i])


# Find '0' location
def find_empty(arr):
    for i in range(3):
        for j in range(3):
            if arr[i][j] == '0':
                return i, j


# find h
def find_h(arr):
    h = 0
    goal = getGoal()
    for i in range(3):
        for j in range(3):
            if arr[i][j] != goal[i][j]:
                h += 1
    return h


def moves():
    return [(1, 0), (0, -1), (-1, 0), (0, 1)]


# print puzzle
def print_final_path(n, original, expand):
    result = []
    while n.arr != original:
        result.insert(0, n.arr)
        n = n.parent
    i = 0
    for arr in result:
        i += 1
        print("---- Move", i, "----")
        print_array(arr)
    print("Total number of moves: ", len(result))
    print("Total number of nodes expanded: ", expand)


class info:
    def __init__(self, arr, parent):
        self.arr = copy.deepcopy(arr)
        self.parent = copy.deepcopy(parent)

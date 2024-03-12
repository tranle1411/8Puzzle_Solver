from BFS import bfs
from BestFirst import bestfirst


# convert 1D array to 2D array
def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]


# print puzzle
def print_array(arr):
    for i in range(3): print(arr[i])


# input txt files
file = {
    1: "very_easy.txt",
    2: "easy.txt",
    3: "medium.txt",
    4: "hard.txt",
    5: "very_hard.txt"
}

# Prompts and Inputs
level = int(input(
    "Welcome to the Puzzle Game. Choose number level 1.very easy, or 2.easy, or 3.medium, or 4.hard, or 5.very hard: "))
if level not in range(1, 6):
    print("Invalid level!")
    exit(1)
f = open(f'inputs/{file[level]}', "r")
arr = f.read().replace('\n', ' ').split(' ')

arr.pop()
arr = convert_1d_to_2d(arr, 3)
print("This is level " + str(level) + " puzzle:")
print_array(arr)

# call BFS and Best First Search
search = int(input("Choose a search method 1. BFS or 2. Best First Search: "))
match search:
    case 1:
        s = bfs(arr)
    case 2:
        s = bestfirst(arr)
    case _:
        print("Invalid search method!")
        exit(1)
s.solve()

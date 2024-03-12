### **README**

**Description:**
The program will use either BFS or Best First Search to determine the path from a given starting state to the goal, as well as how many nodes were expanded during the search.

**The 8-puzzle problem:**
The 8-puzzle is a physical puzzle that involves sliding tiles on a 3x3 grid containing 8 tiles
and an empty spot. You need to slide tiles around in the puzzle until you reach the solution:
1 2 3
8 0 4
7 6 5
The empty spot will be represented by a 0. When determining what moves are possible, you can
only slide tiles adjacent to the empty spot into the empty spot. It is usually easier to consider the
move as moving the empty space, rather than the tile. 

**Instruction:**
- [ ] 1. Download the folder
- [ ] 2. Run `main.py` in any Python Editor (ideally PyCharm or Visual Studio Code with numpy installed)
- [ ] 3. As the prompt is printed, choose a difficulty level by typing down a number from 1 to 5. To see the details of each level, take a look in `very_easy.txt` / `easy.txt` / `medium.txt` / `hard.txt` / `very_hard.txt`
> Welcome to the Puzzle Game. Choose number level 1.very easy, or 2. easy, or 3. medium, or 4.hard, or 5.very hard:
> This is level ___ puzzle: _[insert the puzzle]_
- [ ] 4. As the next prompt is printed, choose a search method by typing down either 1 or 2
> Choose a search method 1. BFS or 2. Best First Search:
- [ ] 5. Wait for the program to run. Every states of the puzzle will be generated while looking for the final goal
- [ ] 6. When the program finish running, the number of nodes expanded and the number of moves will be shown

**File explanation:**
- `main.py` contains all prompts and inputs, as well as calling the search methods. Module used: `bfs `and `bestfirst`
- `BFS.py` contains the BFS (Breath First Search) search method. Modules used: copy, numpy, deque, and `helper`
- `BestFirst.py` contains the Best First Search search method. Modules used: copy, numpy, heapq, and `helper`
- `helper.py` contains `getGoal()` (get the Goal state), `swapPositions()` (swap the position of the '0' with another one), `print_array()` (print out the state), `find_empty()` (locate the '0'), and `find_h()` (calculate heuristic). Module used: copy
- `very_easy.txt` / `easy.txt` / `medium.txt` / `hard.txt` / `very_hard.txt`: contain each level of the puzzle problem

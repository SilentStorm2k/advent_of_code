import time
import sys
from collections import deque

def execute(func):
    def wrapper(*args):   
        t1 = time.time()
        print(f'Answer for {func.__name__} : {func(*args)}')
        t2 = time.time()
        print(f'Executed in : {round(t2-t1, 5)}')
    wrapper.__original = func # if need to reuse p1 w/o decorator use : p1.__original(input)
    return wrapper 


@execute
def p1(input):
    grid = []
    # parsing input and putting it in grid
    rows = input.split('\n')
    for r in rows:
        grid.append(list(r))
    R, C = len(grid)-1, len(grid[0])-1
    start = (0, 1)
    end = (R, C-1)

    sys.setrecursionlimit(2300)
    longestPath = findPath(grid, start, end, set())
    return longestPath-1


slopes = {'>':(0,1), '<':(0,-1), 'v':(1,0), '^':(-1,0)}
def findPath(grid, current, goal, seen):
    R, C = len(grid)-1, len(grid[0])-1
    if current == goal:
        return 1
    if current in seen:
        return 0
    x, y = current[0], current[1]
    tile = grid[x][y]
    # if out of bounds
    if x >= R or x < 0 or y >= C or y < 0:
        return 0
    # on invalid tile
    if tile == '#':
        return 0
    elif tile in slopes.keys():
        seen.add(current)
        dx, dy = slopes.get(tile)
        # return findPath(grid, (x+dx, y+dy), goal, seen)
        return 1+findPath(grid, (x+dx, y+dy), goal, seen)
    else:
        lengths = []
        seen.add(current)
        # bug for longest time : need to send new copy of seen for each path
        newSeen = set(seen)
        for dx, dy in [(0,1), (1,0), (0,-1), (-1, 0)]:
            lengths.append(findPath(grid, (x+dx, y+dy), goal, newSeen))
        return 1+max(lengths)
    
@execute
def p2(input):
    grid = []
    # parsing input and putting it in grid
    rows = input.split('\n')
    for r in rows:
        grid.append(list(r))
    R, C = len(grid)-1, len(grid[0])-1
    for r in range(R+1):
        for c in range(C+1):
            if grid[r][c] in slopes.keys():
                grid[r][c] = '.'
    s = ''
    for r in range(R+1):
        news = "".join(grid[r])
        s = s+news+ ('\n' if r != R else '')
    
    return p1.__original(s)


# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 23/puzzle_input/example.txt" if ex else "2023/day 23/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
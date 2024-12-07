import time
import re
from collections import defaultdict, deque
import heapq

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
    grid, d, start = generateGrid(input)
    path, _ = calculatePath(grid, d, start)
    return len(set(path))

@execute
def p2(input):
    grid, d, start = generateGrid(input)
    path, cycle = calculatePath(grid, d, start)
    blocks = set() 
    for potentialBlock in path:
        if potentialBlock == start or potentialBlock in blocks:
            continue
        i, j = potentialBlock
        grid[i][j] = '#'
        _, cycle = calculatePath(grid, d, start)
        if cycle:
            blocks.add((i,j))
        grid[i][j] = '.'
    return len(blocks) 
 
def calculatePath (grid, d, start):
    path = list()
    seen = set((start, 0))
    idx = 0
    m, n = len(grid), len(grid[0])
    pos = start
    while 0<=pos[0]<m and 0<=pos[1]<n:
        if grid[pos[0]][pos[1]] == '#':
            pos = (pos[0]-d[idx][0], pos[1]-d[idx][1])
            idx = (idx+1)%4
        else:
            if (pos, idx) in seen:
                return [], True
            seen.add((pos, idx))
            path.append(pos)
        pos = (pos[0]+d[idx][0], pos[1]+d[idx][1]) 
    return path, False

def generateGrid (input):
    d = [(-1,0), (0,1), (1,0), (0,-1)]
    grid = []
    pos = (0,0)
    for i, line in enumerate(input.split('\n')):
        row = list(line)
        if '^' in row:
            pos = (i, row.index('^')) 
        grid.append(row)
    return grid, d, pos

def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/06_input.txt", 'r').read()
    example = open("2024/puzzle_input/06_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
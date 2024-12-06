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
    d = [(-1,0), (0,1), (1,0), (0,-1)]
    grid = []
    pos = (0,0)
    for i, line in enumerate(input.split('\n')):
        row = list(line)
        if '^' in row:
            pos = (i, row.index('^')) 
        grid.append(row)
    m, n = len(grid), len(grid[0])
    idx = 0
    seen = set()
    while 0<=pos[0]<m and 0<=pos[1]<n:
        if grid[pos[0]][pos[1]] == '#':
            pos = (pos[0]-d[idx][0], pos[1]-d[idx][1])
            idx = (idx+1)%4
        else:
            seen.add(pos)
        pos = (pos[0]+d[idx][0], pos[1]+d[idx][1]) 
    return len(seen) 
                 
@execute
def p2(input):
    return None
 


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
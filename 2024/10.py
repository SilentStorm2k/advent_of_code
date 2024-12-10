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
def p1(input, p2 = False):
    grid = []
    start = [] 
    for i, line in enumerate(input.split('\n')):
        zeros = re.finditer(r'0', line)
        for j in zeros:
            start.append((i,j.start()))
        line = [int(ele) for ele in line]
        grid.append(line)
        
    m, n = len(grid), len(grid[0])
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    trailEnds = set()
    rating = 0

    def dfs (i, j, seen):
        nonlocal trailEnds, rating
        if grid[i][j] == 9:
            trailEnds.add((i,j))
            rating += 1
            return
        for dr, dc in d:
            if not (0 <= i+dr < m and 0 <= j+dc < n): 
                continue
            if grid[i][j]+1 == grid[i+dr][j+dc] and (i+dr, j+dc) not in seen:
                seen.add((i+dr, j+dc))
                dfs (i+dr, j+dc, seen) 
                seen.remove((i+dr, j+dc))

    res = 0
    for r, c in start:
        trailEnds = set() 
        rating = 0
        dfs (r, c, set())
        if p2:
            res += rating
        else:
            res += len(trailEnds)
        
    return res 
                 
@execute
def p2(input):
    return p1.__original(input, p2=True)

def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/10_input.txt", 'r').read()
    example = open("2024/puzzle_input/10_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
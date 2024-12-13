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
def p1(input, p2=False):
    grid = []
    for row in input.split('\n'):
        grid.append(list(row))
    seen = set()
    curSeen = set()
    corners = list()
    edges = defaultdict(int)
    m, n = len(grid), len(grid[0])

    def dfs (i, j, region):
        if  not (0 <= i < m and 0 <= j < n) or \
            grid[i][j] != region:
            edges[(i,j)] += 1
            return
        if  (i,j) in seen or (i,j) in curSeen: 
            return
        seen.add((i,j))
        curSeen.add((i,j))
        for _ in range(isCorner(i,j)):
            # (i,j) can host multiple vertices (so accounting for that)
            corners.append((i,j)) 
        
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs (i+di, j+dj, region)
    
    def isCorner (i,j):
        d = [(1,1),(1,-1),(-1,1),(-1,-1)] 
        cornerCount = 0
        for di, dj in d:
            if 0<=i+di<m and 0<=j+dj<n:
                if grid[i][j] != grid[i+di][j+dj] and grid[i][j] == grid[i+di][j] and grid[i][j] == grid[i][j+dj]:
                    cornerCount += 1
                if grid[i][j] != grid[i+di][j] and grid[i][j] != grid[i][j+dj]:
                    cornerCount += 1
            else:
                if 0<=i+di<m and grid[i][j] != grid[i+di][j]:
                    cornerCount += 1
                if 0<=j+dj<n and grid[i][j] != grid[i][j+dj]:
                    cornerCount += 1
                if not (0<=i+di<m) and not (0<=j+dj<n):
                    cornerCount += 1
        return cornerCount
             
    res = 0
    for i in range(m):
        for j in range(n):
            curSeen = set()
            edges = defaultdict(int)
            corners = list()
            perimeter = 0
            dfs (i, j, grid[i][j])
            if curSeen:
                sides = len(corners)
                perimeter = sum(edges.values()) 
                res += len(curSeen)*(sides if p2 else perimeter)
    return res  
                 
@execute
def p2(input):
    return p1.__original(input, p2=True)

def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/12_input.txt", 'r').read()
    example = open("2024/puzzle_input/12_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
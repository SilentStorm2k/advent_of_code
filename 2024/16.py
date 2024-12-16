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
    # want to minimize turns (prefer straight paths)
    # lets do dijkstras later, only bfs for now
    grid = [list(row) for row in input.split('\n')]
    m, n = len(grid), len(grid[0])
    start, end = (), ()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                start = (i,j)
            if grid[i][j] == 'E':
                end = (i,j)
                
    q = deque()
    q.append((start, (1,0), set(), 0))
    scores = []
    while q: 
        nodes = len(q)
        print(nodes)
        for _ in range(nodes):
            cur = q.popleft()
            pos, dir, seen, curScore = cur
            i, j = pos
            if pos in seen or grid[i][j] == '#':
                continue
            seen.add(pos)
            if pos == end:
                scores.append(curScore)
            else:
                for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
                    if 0 <= i+di < m and 0 <= j+dj < n:
                        q.append(((i+di, j+dj), (di,dj), set(seen), curScore + (1 if (di,dj) == dir else 1001)))
    
    return min(scores) 
                 
@execute
def p2(input):
    return None
 


def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/16_input.txt", 'r').read()
    example = open("2024/puzzle_input/16_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    # p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
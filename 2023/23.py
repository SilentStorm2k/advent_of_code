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

    sys.setrecursionlimit(10000)
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
    start = (0, 1)
    end = (R, C-1)
    for r in range(R+1):
        for c in range(C+1):
            if grid[r][c] in slopes.keys():
                grid[r][c] = '.'
    

    nodes = [start, end]
    for r, row in enumerate(grid):
        for c, tile in enumerate(row):
            if tile == '#':
                continue
            neighbors = 0
            for nr, nc in [(r,c+1), (r,c-1), (r+1, c), (r-1,c)]:
                if 0<=nr<=R and 0<=nc<=C and grid[nr][nc] != '#':
                    neighbors += 1
                
            if neighbors >= 3:
                nodes.append((r, c))
    
    graph = {node: {} for node in nodes}

    for sr, sc in nodes:
        stack = [(sr, sc, 0)]
        seen = {(sr,sc)}
        while stack:
            r, c, dist = stack.pop()
            if dist != 0 and (r, c) in nodes:
                graph[(sr, sc)][(r, c)] = dist
                continue

            for dr, dc in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nr = r+dr
                nc = c+dc
                if 0<=nr<=R and 0<=nc<=C and grid[nr][nc] != '#' and (nr, nc) not in seen:
                    stack.append((nr, nc, dist+1))
                    seen.add((nr, nc))

    seen = set()
    def dfs(node):
        if node == end:
            return 0
        m = -float("inf")

        seen.add(node)
        for nx in graph[node]:
            if nx not in seen:
                m = max(m, dfs(nx) + graph[node][nx])
        seen.remove(node)
        return m

    return dfs(start)


        

def main():
    # when called from ~/Code/repos/advent_of_code$
    input = open("2023/day 23/puzzle_input/input.txt", 'r').read()
    example = open("2023/day 23/puzzle_input/example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
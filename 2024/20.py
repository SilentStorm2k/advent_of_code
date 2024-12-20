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
    input = input.split('\n')
    grid = []
    start, end = (), ()
    for i, row in enumerate(input):
        if 'S' in row:
            start = (i,row.index('S'))
        if 'E' in row:
            end = (i, row.index('E'))
        grid.append(list(row))

    # timeTaken = bfs(grid, start, end)
    timeTaken = dijkstras(grid, start, end)
    cheatedSpots = set()
    cheatPos = (0,0) 
    res = 0
    while cheatPos != (-1,-1):
        curTime, cheatPos = dijkstrasCheat(grid, start, end, cheatedSpots)
        cheatedSpots.add(cheatPos)
        res += 1 if curTime <= timeTaken-100 else 0
        if res % 100 == 0:
            print(res)
    
    return res
    
    
def dijkstrasCheat (grid, start, end, cheated):
    q = []
    m, n = len(grid), len(grid[0])
    dists = {} 
    seen = set()
    direc = [(0,1), (1,0), (0,-1), (-1,0)]
    cheatPos = (-1,-1)
    heapq.heappush(q, (0, start)) # dist, position, isCheatAllowed
    while q:
        dist, pos = heapq.heappop(q)
        if pos == end:
            return dist, cheatPos
        x, y = pos
        seen.add(pos)
        for dx, dy in direc: 
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in seen:
                if grid[nx][ny] == '#' and (nx,ny) not in cheated and cheatPos == (-1,-1):
                    cheatPos = (nx,ny) 
                    if (nx,ny) not in dists:
                        dists[(nx,ny)] = dist+1
                    dists[(nx,ny)] = min(dists[(nx,ny)], dist+1)
                    heapq.heappush(q, (dists[(nx,ny)], (nx,ny)))
                elif grid[nx][ny] != '#':
                    if (nx,ny) not in dists:
                        dists[(nx,ny)] = dist+1
                    dists[(nx,ny)] = min(dists[(nx,ny)], dist+1)
                    heapq.heappush(q, (dists[(nx,ny)], (nx,ny)))
                else:
                    continue
    return -1, (-1,-1)
 

def dijkstras (grid, start, end):
    q = []
    m, n = len(grid), len(grid[0])
    dists = {} 
    seen = set()
    direc = [(0,1), (1,0), (0,-1), (-1,0)]
    heapq.heappush(q, (0, start)) # dist, position, isCheatAllowed
    while q:
        dist, pos = heapq.heappop(q)
        if pos == end:
            return dist
        x, y = pos
        seen.add(pos)
        for dx, dy in direc: 
            nx, ny = x+dx, y+dy
            if 0<=nx<m and 0<=ny<n and (nx,ny) not in seen and grid[nx][ny] != '#':
                if (nx,ny) not in dists:
                    dists[(nx,ny)] = dist+1
                dists[(nx,ny)] = min(dists[(nx,ny)], dist+1)
                heapq.heappush(q, (dists[(nx,ny)], (nx,ny)))
    return -1
                 
@execute
def p2(input):
    input = input.split('\n')
    grid = []
    start, end = (), ()
    for i, row in enumerate(input):
        if 'S' in row:
            start = (i,row.index('S'))
        if 'E' in row:
            end = (i, row.index('E'))
        grid.append(list(row))

    # timeTaken = bfs(grid, start, end)
    timeTaken = dijkstras(grid, start, end)
    cheatedSpots = set()
    cheatPos = (0,0) 
    res = 0
    while cheatPos != (-1,-1):
        curTime, cheatPos = dijkstrasCheat(grid, start, end, cheatedSpots)
        cheatedSpots.add(cheatPos)
        res += 1 if curTime <= timeTaken-100 else 0
        if res % 100 == 0:
            print(res)
    
    return res
 


def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/20_input.txt", 'r').read()
    example = open("2024/puzzle_input/20_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
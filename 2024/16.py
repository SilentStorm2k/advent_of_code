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
                
    # q = deque()
    q = []
    res = []
    # q.append((start, (1,0), set(), 0))
    heapq.heappush(q, (0, start, (1,0)))
    visit = { (start, (1,0)) : 0} 
    while q:
        score, pos, dir = heapq.heappop(q) 
        i, j = pos
        if visit.get((pos,dir), float('inf')) < score:
            continue
        for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            if di==-dir[0] and dj==-dir[1]:
                continue
            nScore = score 
            ni, nj = i, j
            nDir = (di,dj)
            if nDir == dir:
                ni, nj = i+di, j+dj
                nScore += 1
            else:
                nScore += 1000
            
            nPos = (ni, nj)
            if 0 <= ni < m and 0 <= nj < n and nScore < visit.get((nPos, nDir), float('inf')) and grid[ni][nj] != '#':
                # pushing only when there is cost increment
                visit[((nPos, nDir))] = nScore
                heapq.heappush(q, (nScore, nPos, nDir))
    
    visited = dijkstra(grid, start, end, m, n)
    res = float('inf')
    for d in [(0,1),(1,0),(0,-1),(-1,0)]:
        print(visit.get((end,d), float('inf'))- 1000)
        res = min(res, visit.get((end,d), float('inf')))
    
    for d in range(4):
        # print(visited.get((end[0], end[1], d), float('inf')))
        res = min(res, visited.get((end[0], end[1], d), float('inf')))

    return res 
            

        
        
    # scores = []
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
 

def dijkstra(grid, start, end, rows, cols):
    """Run Dijkstra's algorithm to find minimum costs and visited states."""
    # Directions: N=0, E=1, S=2, W=3
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    start_state = (start[0], start[1], 1)  # Start facing East

    # Priority queue and visited dictionary
    pq = []
    heapq.heappush(pq, (0, start_state))
    visited = {start_state: 0}

    while pq:
        cost, (x, y, d) = heapq.heappop(pq)

        # Skip if we've already processed a better cost for this state
        if visited.get((x, y, d), float('inf')) < cost:
            continue

        # Move forward
        dx, dy = directions[d]
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
            new_cost = cost + 1
            if new_cost < visited.get((nx, ny, d), float('inf')):
                visited[(nx, ny, d)] = new_cost
                heapq.heappush(pq, (new_cost, (nx, ny, d)))

        # Turn left or right
        for nd in [(d - 1) % 4, (d + 1) % 4]:
            new_cost = cost + 1000
            if new_cost < visited.get((x, y, nd), float('inf')):
                visited[(x, y, nd)] = new_cost
                heapq.heappush(pq, (new_cost, (x, y, nd)))

    return visited

def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/16_dummy.txt", 'r').read()
    example = open("2024/puzzle_input/16_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
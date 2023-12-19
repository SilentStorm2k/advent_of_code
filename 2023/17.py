import time
from heapq import heappop, heappush

def execute(func):
    def wrapper(*args):   
        t1 = time.time()
        print(f'Answer for {func.__name__} : {func(*args)}')
        t2 = time.time()
        print(f'Executed in : {round(t2-t1, 5)}')
    wrapper.__original = func # if need to reuse p1 w/o decorator use : p1.__original(input)
    return wrapper 

@execute
def p1(input, mn = 0, mx = 3):
    input = input.split('\n')
    rows = [[] for _ in range(len(input))]
    for r, row in enumerate(input):
        rows[r] = [int(ele) for ele in row]
    
    R, C = len(rows)-1, len(rows[0])-1
    seen = set()
    pq = [(0, 0, 0, 0, 1, 0)]
    minHeatLoss = 0
    # implementation of dijkstra algorithm
    while pq:
        # using heap (priority queue) to store state (heat loss, x, y coord, dx, dy, and n = number of times we've gone straight)
        hl, r, c, dr, dc, n = heappop(pq)

        # heat loss always minimum value since its a pq
        if r==R and c==C and n >= mn:
            minHeatLoss = hl
            break

        # having seen set to eliminate loops (not including heat loss as we do not want to add additional heat loss if cycle)
        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))

        # if going in straight line less than the max allowed straight line dist (mx) add to heap
        if n < mx:
            nr = r+dr
            nc = c+dc
            if 0<=nr<=R and 0<=nc<=C:
                heappush(pq, (hl+rows[nr][nc], nr, nc, dr, dc, n+1))
        
        # changing direction under the valid conditions (not turning back, not going straight, and > min allowed straight distance crossed)
        for ndr, ndc in [(0,1), (1,0), (-1,0), (0,-1)]:
            if (ndr, ndc) != (-dr, -dc) and (ndr, ndc) != (dr, dc) and n >= mn:
                nr = r+ndr
                nc = c+ndc
                if 0<=nr<=R and 0<=nc<=C:
                    heappush(pq, (hl+rows[nr][nc], nr, nc, ndr, ndc, 1))
    return minHeatLoss


@execute
def p2(input):
    return p1.__original(input, 4, 10)

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 17/puzzle_input/example.txt" if ex else "2023/day 17/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)

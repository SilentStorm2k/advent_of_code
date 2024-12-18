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
def p1(input, start=(0,0), end=(70,70), fallenBytes = 1024):
    incomingBytes = input.split('\n')
    m, n = end
    q = deque()
    q.append((start[0], start[1], set()))
    bytePos = set()
    for i in range(fallenBytes):
        fx, fy = incomingBytes[i].split(',')
        fx, fy = int(fx), int(fy)
        bytePos.add((fx,fy))
    return shortestPathCost(bytePos, end, m, n) 
                 
@execute
def p2(input, start = (0,0), end = (70,70), shortcut = 0):
    incomingBytes = input.split('\n')
    m, n = end
    q = deque()
    q.append((start[0], start[1], set()))
    bytePos = set()
    for i in range(len(incomingBytes)):
        fx, fy = incomingBytes[i].split(',')
        fx, fy = int(fx), int(fy)
        bytePos.add((fx,fy))
        if shortestPathCost(bytePos, end, m, n) == -1 and i > shortcut:
            return f"{fx},{fy}"
    return -1 
 
def shortestPathCost (bytePos, end, m, n):
    # implement dijkstras
    heap = []
    heapq.heappush(heap, (0,0,0))
    seen = set()
    costs = {(0,0):0}
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    while heap:
        steps, x, y = heapq.heappop(heap)
        if (x,y) in seen:
            continue
        if (x,y) == end:
            return steps
        seen.add((x,y))
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if 0 <= nx <= m and 0 <= ny <= n and (nx, ny) not in bytePos:
                if steps + 1 < costs.get((nx,ny), float('inf')):
                    costs[(nx,ny)] = steps+1
                    heapq.heappush(heap, (costs[(nx,ny)], nx, ny))
    return -1



def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/18_input.txt", 'r').read()
    example = open("2024/puzzle_input/18_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example, (0,0), (6,6), 12)
    p1(input)
    print("\nPart 2:")
    p2(example, (0,0), (6,6))
    p2(input)

if __name__ == "__main__":
    main()
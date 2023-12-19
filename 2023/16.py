import time
from collections import defaultdict

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
    for line in input:
        grid.append(list(line))
    start = (0,0)
    pre = (0, -1)
    ret = call(grid, start,pre)
    return ret
@execute
def p2(input):
    input = input.split('\n')
    grid = []
    for line in input:
        grid.append(list(line))
    start = (0,0)
    pre = (0, -1)
    ret = set()
    for r in range(len(grid)):
        start = (r,0)
        pre = (r,-1)
        ret.add(call(grid, start,pre))
        start = (r,len(grid[0])-1)
        pre = (r,len(grid[0]))
        ret.add(call(grid, start,pre))
    for c in range(len(grid[0])):
        start = (0,c)
        pre = (-1,c)
        ret.add(call(grid, start,pre))
        start = (len(grid)-1,c)
        pre = (len(grid),c)
        ret.add(call(grid, start,pre))
    return max(ret)

def call(grid, start, pre):
    R, C = len(grid), len(grid[0])
    visited = set()
    i, j = start[0], start[1]
    # pre = (i,j-1)
    visited.add((i,j))
    toExplore = {(i,j,pre)}
    oldlen, timer = 0, 0
    while True:
        newExplore = set()
        for l in toExplore:
            i, j ,pre = l[0], l[1], l[2]
            if i < 0 or i >= R or j < 0 or j >= C:
                continue
            inext, jnext, t1, t2, split = getDirection(i, j ,pre, grid[i][j])
            # print(getDirection(i, j ,pre, grid[i][j]))
            cur = (i,j)
            visited.add(cur)
            if split:
                newExplore.add((t1,t2,cur))
            newExplore.add((inext, jnext,cur))
        toExplore = newExplore
        newlen = len(visited)
        if newlen == oldlen:
            timer +=1
        oldlen = newlen
        if timer >= 50:
            break
    return len(visited)


def getDirection(i, j, pre, val):
    # from left
    if pre == (i, j-1):
        if val == '.' or val == '-':
            return i, j+1, 0, 0, False
        if val == '\\':
            return i+1, j, 0, 0, False
        if val == '/':
            return i-1, j, 0, 0, False
        if val == '|':
            return i-1, j, i+1, j, True
    # from right
    if pre == (i, j+1):
        if val == '.' or val == '-':
            return i, j-1, 0, 0, False
        if val == '\\':
            return i-1, j, 0, 0, False
        if val == '/':
            return i+1, j, 0, 0, False
        if val == '|':
            return i-1, j, i+1, j, True
    # from top
    if pre == (i-1, j):
        if val == '.' or val == '|':
            return i+1, j, 0, 0, False
        if val == '\\':
            return i, j+1, 0, 0, False
        if val == '/':
            return i, j-1, 0, 0, False
        if val == '-':
            return i, j-1, i, j+1, True
    # from bottom
    if pre == (i+1, j):
        if val == '.' or val == '|':
            return i-1, j, 0, 0, False
        if val == '\\':
            return i, j-1, 0, 0, False
        if val == '/':
            return i, j+1, 0, 0, False
        if val == '-':
            return i, j-1, i, j+1, True
    return -1, -1, 0, 0, False


# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 16/puzzle_input/example.txt" if ex else "2023/day 16/puzzle_input/input.txt", 'r').read()
p1(input) # runs in 0.5 s
p2(input) # runs in 200 s
import time

def execute(func):
    def wrapper(*args):   
        t1 = time.time()
        print(f'Answer for {func.__name__} : {func(*args)}')
        t2 = time.time()
        print(f'Executed in : {round(t2-t1, 5)}')
    wrapper.__original = func # if need to reuse p1 w/o decorator use : p1.__original(input)
    return wrapper 

@execute
def p1(input, steps = 64):
    input = input.split('\n')
    grid = []
    start = (0,0)
    for r, row in enumerate(input):
        grid.append(list(row))
        if 'S' in row:
            start = (r, row.index('S'))
    state = set()
    state.add(start)
    ret = countStates(grid, {start}, steps)  
    return ret

t = []
def countStates(grid, state, steps):
    R, C = len(grid), len(grid[0])
    length, step = 1, 0
    while step < steps:
        retState = set()
        for coord in state:
            x,y = coord 
            l, r, u, d = (x-1, y), (x+1, y), (x, y-1), (x, y+1)
            if grid[l[0]%R][l[1]%C] != '#' : retState.add(l)
            if grid[r[0]%R][r[1]%C] != '#' : retState.add(r)
            if grid[u[0]%R][u[1]%C] != '#' : retState.add(u)
            if grid[d[0]%R][d[1]%C] != '#' : retState.add(d)
        length += (len(retState) - len(state))
        state = retState
        step += 1
    return length

# number oscillates bw 7193 (even) and 7082 (odd) for large inputs for individual grid
# the center ones which will likely be filled will have either of the above 2 nos
@execute
def p2(input):
    steps = 100
    # steps = 26501365
    return p1.__original(input, steps)

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 21/puzzle_input/example.txt" if ex else "2023/day 21/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
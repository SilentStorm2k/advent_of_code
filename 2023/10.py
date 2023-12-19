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
def p1(input):
    coords = [list(r) for r in input.split('\n')]
    for i, r in enumerate(coords):
        for j, c in enumerate(r):
            if c == 'S':
                start = (i, j)
    dist = 1
    visited = {start}
    cur = get_next(coords, start, visited)
    count = 10
    while (cur != None):
        visited.add(cur)
        dist += 1
        cur = get_next(coords, cur, visited)
        count -= 1
    return dist//2


@execute
def p2(input):
    coords = [list(r) for r in input.split('\n')]
    for i, r in enumerate(coords):
        for j, c in enumerate(r):
            if c == 'S':
                start = (i, j)
    visited = {start}
    cur = get_next(coords, start, visited)
    while (cur != None):
        visited.add(cur)
        cur = get_next(coords, cur, visited)
    visited = sorted(visited)

    op = False
    area = 0
    up_down = ['|', '7', 'F', 'S']
    for i, r in enumerate(coords):
        s = ''
        for j, c in enumerate(r): 
            if (i,j) in visited:
                if coords[i][j] in up_down:
                    op = not op
                    s += coords[i][j]
                else:
                    s += coords[i][j]
            elif op:
                s += '1'
                area += 1
            else:
                s += '0'
        # print(s)

    return area

above = ['|', '7', 'F']
right = ['-', '7', 'J']
below = ['|', 'J', 'L']
left = ['-', 'L', 'F']
directions = {'|' : [(-1, 0), (1,0)], '-' : [(0, -1), (0,1)], 'L' : [(-1, 0), (0,1)], 'J' : [(-1, 0), (0,-1)], '7' : [(1, 0), (0,-1)], 'F' : [(1, 0), (0,1)]}
def get_next(coords, start, visited):
    i, j = start[0], start[1]
    if coords[i][j] == 'S':
        if coords[i-1][j] in above:
            return (i-1,j)
        if coords[i][j+1] in right:
            return (i,j+1)
        if coords[i+1][j] in below:
            return (i+1,j)
        if coords[i][j-1] in left:
            return (i,j-1)
    
    next = directions.get(coords[i][j])
    if (i+next[0][0], j+next[0][1]) not in visited:
        return (i+next[0][0], j+next[0][1])
    elif (i+next[1][0], j+next[1][1]) not in visited:
        return (i+next[1][0], j+next[1][1])
    else:
        return None
    
# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 10/puzzle_input/example4.txt" if ex else "2023/day 10/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
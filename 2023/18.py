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
def p1(input, part1 = True):
    input = input.split('\n')
    direc, steps, dxy = [], [], []
    for inp in input:
        if part1: 
            d, s, c = inp.split(' ')
            direc.append(d)
        else :
            c = inp.split(' ')[2]
            direc.append(c[-2])
            s = int(c[2:len(c)-2], 16)
        steps.append(s)
    steps = [int(i) for i in steps]
    for i, d in enumerate(direc):
        if d == 'R' or d == '0':
            dx, dy = 1, 0
        if d == 'L' or d == '2':
            dx, dy = -1, 0
        if d == 'U' or d == '3':
            dx, dy = 0, 1
        if d == 'D' or d == '1':
            dx, dy = 0, -1
        dx *= int(steps[i])
        dy *= int(steps[i])
        dxy.append((dx,dy))
    
    # applying shoelace formula to get all the inner points
    area = 0
    x1, y1 = 0, 0
    for diff in dxy:
        dx, dy = diff[0], diff[1]
        x2, y2 = x1+dx, y1+dy
        area += (-x1*y2 + x2*y1)/2 
        x1, y1 = x2, y2

    # picks theorem -> A = i + b/2 -1
    # inner pts + boundary pts/2 (perimeter here) - 1
    # rearranging we get -> i = A - b/2 + 1
    # we need to find answer which is inner points + boundary points area = i + b
    # then ans = A - b/2 + 1 + b -> A + b/2 + 1
    return int(abs(area) + (sum(steps)/2) + 1)

@execute
def p2(input):
    return p1.__original(input, False)

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 18/puzzle_input/example.txt" if ex else "2023/day 18/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
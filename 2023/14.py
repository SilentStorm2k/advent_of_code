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
    rows = input.split('\n')
    prob = [[c for c in row] for row in rows]
    # rolling north
    prob = roll(prob)
    # and getting the score
    sum = score(prob)
    return sum

@execute
def p2(input):
    rows = input.split('\n')
    prob = [[c for c in row] for row in rows]
    sum = 0
    allsum = defaultdict(list)
    cycle, cyc = 0, -1
    # pattern recognition
    # since the sums after rotations eventually repeat
    # we look for patterns of reoccurrence
    # when a sum gets repeated (here 8 times) up to a critical thresh hold
    # we know that it will eventually repeat again, and get the corresponding repeat value
    while cycle <= 1000:
        cycle += 1
        # rotate and roll 4 times
        for i in range(4):
            prob = roll(prob)
            prob = rotate(prob)
        # get its score
        sum = score(prob)
        # add the score to our dict of score trackers (score -> cycle it was seen at)
        allsum[sum].append(cycle)

        # if said score appears more than 8 times, we are reasonably confident that there is a repeat
        if len(allsum[sum]) >= 8:
            check = allsum[sum]
            diff = check[1]-check[0]
            c = 0
            # checking whether the repeats are at regular intervals
            for i in range(2, len(check)):
                newdiff = check[i]-check[i-1]
                if diff != newdiff:
                    break
                c = i
            # if so, then getting the closest cycle value which will match the 1000000000th cycle
            if c == len(check)-1:
                cyc = cycle + (1000000000-cycle)%diff
            if cycle==cyc:
                return sum
    return 0

def rotate(input):
    R = len(input)
    C = len(input[0])
    ret = [['?' for i in range(R)] for j in range(C)]
    for r in range(R):
        for c in range(C):
            ret[c][R-1-r] = input[r][c]
    return ret

def roll(input):
    R = len(input)
    C = len(input[0])
    empty_slots = [0 for i in range(C)]
    for i in range(R):
        for j in range(C):
            if input[i][j] == '.':
                empty_slots[j] += 1
            if input[i][j] == 'O':
                if empty_slots[j] != 0:
                    input[i-empty_slots[j]][j] = 'O'
                    input[i][j] = '.'
            if input[i][j] == '#':
                empty_slots[j] = 0
    return input

def score(input):
    ans = 0
    R = len(input)
    C = len(input[0])
    for i in range(R):
        for j in range(C):
            if input[i][j] == 'O':
                ans += R-i
    return ans

def show(input):
    for r in range(len(input)):
        print(''.join(input[r]))
# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 14/puzzle_input/example.txt" if ex else "2023/day 14/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
import time
import re
import numpy as np
import math

def execute(func):
    def wrapper(*args):   
        t1 = time.time()
        print(f'Answer for {func.__name__} : {func(*args)}')
        t2 = time.time()
        print(f'Executed in : {round(t2-t1, 5)}')
    wrapper.__original = func # if need to reuse p1 w/o decorator use : p1.__original(input)
    return wrapper 

@execute
def p1(input, start, end):
    ins, coords = input.split('\n\n')
    coord = {c[0] : (c[1], c[2]) for cur in coords.split('\n') if (c := re.findall(r'[A-Z0-9]+', cur))}
    cur, index, steps = start, 0, 0
    while (re.fullmatch(end, cur) == None):             # while current not at end
        direction = 1 if ins[index] == 'R' else 0       # for left or right
        index += 1 if index != len(ins)-1 else -index   # increment or loopback
        cur = coord[cur][direction]                     
        steps += 1
    return steps

@execute
def p2(input):
    ins, coords = input.split('\n\n')
    coord = {c[0] : (c[1], c[2]) for cur in coords.split('\n') if (c := re.findall(r'[A-Z0-9]+', cur))}
    cur = [cor for cor in coord.keys() if re.fullmatch(r'(..A)', cor)]  # list of all possible starting coords
    min_steps = [p1.__original(input, c, r'(..Z)') for c in cur]        # calculating steps for each starting coord
    return math.lcm(*min_steps)                                         # total traversal len is the lcm of all traversal len

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 8/puzzle_input/example.txt" if ex else "2023/day 8/puzzle_input/input.txt", 'r').read()
p1(input, 'AAA', r'(ZZZ)')
p2(input)
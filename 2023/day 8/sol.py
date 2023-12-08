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
    coord = {re.findall(r'[A-Z0-9]+', cur)[0] : (re.findall(r'[A-Z0-9]+', cur)[1], re.findall(r'[A-Z0-9]+', cur)[2]) for cur in coords.split('\n')}
    cur = start
    index, steps = 0, 0
    while (re.fullmatch(end, cur) == None):
        direction = 1 if ins[index] == 'R' else 0
        index += 1
        index = 0 if index == len(ins) else index 
        cur = coord[cur][direction]
        steps += 1
    return steps

@execute
def p2(input):
    ins, coords = input.split('\n\n')
    coord = {re.findall(r'[A-Z0-9]+', cur)[0] : (re.findall(r'[A-Z0-9]+', cur)[1], re.findall(r'[A-Z0-9]+', cur)[2]) for cur in coords.split('\n')}
    cur = [cor for cor in coord.keys() if re.fullmatch(r'(..A)', cor)]
    min_steps = [p1.__original(input, c, r'(..Z)') for c in cur]
    return math.lcm(*min_steps)

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 8/puzzle_input/example.txt" if ex else "2023/day 8/puzzle_input/input.txt", 'r').read()
p1(input, 'AAA', r'(ZZZ)')
p2(input)
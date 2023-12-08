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
def p1(input):
    ins, coords = input.split('\n\n')
    coord = {re.findall(r'[A-Z]+', cur)[0] : (re.findall(r'[A-Z]+', cur)[1], re.findall(r'[A-Z]+', cur)[2]) for cur in coords.split('\n')}
    cur, ed = 'AAA', 'ZZZ'
    index, steps = 0, 0
    while (cur != ed):
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
    index, steps = 0, 0
    min_steps = np.zeros(len(cur), dtype=np.int32)
    while (True):
        direction = 1 if ins[index] == 'R' else 0
        index += 1
        index = 0 if index == len(ins) else index 
        cur = [coord[c][direction] for c in cur]
        steps += 1

        # print(cur)
        if steps % 1000000 == 0:
            print(steps)
        for i, c in enumerate(cur):
            if re.fullmatch(r'(..Z)', c) != None:
                min_steps[i] = min_steps[i] if min_steps[i] != 0 else steps
        count = 0
        for m in min_steps:
            if m != 0:
                count +=1
        if count == len(cur):
            break

    return math.lcm(*min_steps)

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 8/puzzle_input/example.txt" if ex else "2023/day 8/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
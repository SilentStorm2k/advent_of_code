from pulp import *
import time
import re
from collections import defaultdict, deque
import heapq
import numpy as np

def execute(func):
    def wrapper(*args):   
        t1 = time.time()
        print(f'Answer for {func.__name__} : {func(*args)}')
        t2 = time.time()
        print(f'Executed in : {round(t2-t1, 5)}')
    wrapper.__original = func # if need to reuse p1 w/o decorator use : p1.__original(input)
    return wrapper 


@execute
def p1(input, offset=0):
    res = 0
    for clawMachine in input.split('\n\n'):
        clawMachine = clawMachine.split('\n')
        buttonA, buttonB, prize = clawMachine
        buttonA = [int(ele.strip().split('+')[1]) for ele in buttonA.split(':')[1].split(',')]
        buttonB = [int(ele.strip().split('+')[1]) for ele in buttonB.split(':')[1].split(',')]
        prize = [int(ele.strip().split('=')[1])+offset for ele in prize.split(':')[1].split(',')]
        x1, y1 = buttonA
        x2, y2 = buttonB
        p1, p2 = prize
        
        # linear equation in 2 variables (can use substitution method as shown below) 
        b = (p2*x1-p1*y1)/(x1*y2-x2*y1)
        a = (p1-b*x2)/x1
        if a == int(a) and b == int(b):
            # only add if we get integer solution
            res += int(3*a+b)
 
    return res 
                 
@execute
def p2(input):
    return p1.__original(input, offset=10000000000000)


def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/13_input.txt", 'r').read()
    example = open("2024/puzzle_input/13_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
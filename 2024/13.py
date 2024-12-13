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
def p1(input):
    res = 0
    for clawMachine in input.split('\n\n'):
        clawMachine = clawMachine.split('\n')
        buttonA, buttonB, prize = clawMachine
        buttonA = [int(ele.strip().split('+')[1]) for ele in buttonA.split(':')[1].split(',')]
        buttonB = [int(ele.strip().split('+')[1]) for ele in buttonB.split(':')[1].split(',')]
        prize = [int(ele.strip().split('=')[1]) for ele in prize.split(':')[1].split(',')]

        a = LpVariable("a", lowBound=0, cat='Integer')
        b = LpVariable("b", lowBound=0, cat='Integer') 
        
        prob = LpProblem("Minimize button presses", LpMinimize)
        prob += 3*a+b
        
        # constraints
        prob += a*buttonA[0] + b*buttonB[0] == prize[0]
        prob += a*buttonA[1] + b*buttonB[1] == prize[1]
        
        prob.solve(PULP_CBC_CMD(msg=0))
        # pulp.PULP_CBC_CMD(msg=False).solve(prob)
        if LpStatus[prob.status] == "Optimal":
            res += int(value(prob.objective))

    return res 
                 
@execute
def p2(input):
    res = 0
    for clawMachine in input.split('\n\n'):
        clawMachine = clawMachine.split('\n')
        buttonA, buttonB, prize = clawMachine
        buttonA = [int(ele.strip().split('+')[1]) for ele in buttonA.split(':')[1].split(',')]
        buttonB = [int(ele.strip().split('+')[1]) for ele in buttonB.split(':')[1].split(',')]
        prize = [int(ele.strip().split('=')[1]) + 10000000000000 for ele in prize.split(':')[1].split(',')]

        buttons = np.array([buttonA, buttonB])
        prize   = np.array(prize)
        
        try:
            inverse = np.linalg.inv(buttons)
        except np.linalg.LinAlgError:
            continue

        potRes = inverse @ prize 
        # print(potRes)
        res += 3*potRes[0] + potRes[1]


        # print(buttonA, buttonB, prize)
        # a = LpVariable("a", lowBound=0, cat='Integer')
        # b = LpVariable("b", lowBound=0, cat='Integer') 
        
        # prob = LpProblem("Minimize button presses", LpMinimize)
        # prob += 3*a+b
        # # constraints
        # prob += a*buttonA[0] + b*buttonB[0] == prize[0]
        # prob += a*buttonA[1] + b*buttonB[1] == prize[1]
        
        # prob.solve(PULP_CBC_CMD(msg=0))
        # # pulp.PULP_CBC_CMD(msg=False).solve(prob) 
        # # print(LpStatus[prob.status]) 
        # # print(value(a), value(b))
        # if LpStatus[prob.status] == "Optimal":
        #     res += int(value(prob.objective))

    return res 


def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/13_input.txt", 'r').read()
    example = open("2024/puzzle_input/13_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    # p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
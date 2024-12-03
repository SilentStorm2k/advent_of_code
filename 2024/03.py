import time
import re
from collections import defaultdict, deque
import heapq

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
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)
    res = sum([int(a)*int(b) for a, b in matches])
    return res
                 
@execute
def p2(input):
    input = input.split("don't()")
    res = p1.__original(input[0]) 
    for inp in input:
        curInp = inp.split("do()", 1)
        res += p1.__original(curInp[1]) if len(curInp) == 2 else 0
    return res
 


def main():
    # when called from ~/Code/repos/advent_of_code$
    input = open("2024/puzzle_input/03_input.txt", 'r').read()
    example = open("2024/puzzle_input/03_example.txt", 'r').read()
    example2 = open("2024/puzzle_input/03_example2.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example2)
    p2(input)

if __name__ == "__main__":
    main()
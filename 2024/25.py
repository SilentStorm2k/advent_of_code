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
    r = 0
    c = 0
    locks = set() 
    keys = set()
    for inp in input.split('\n\n'):
        lock = False
        if inp[0] == '#':
            lock = True
        if not r and not c:
            r = len(inp.split('\n'))
            c = len(inp.split('\n')[0])
        grid = [0]*c
        for row in inp.split('\n'):
            for i, ele in enumerate(list(row)):
                grid[i] += 1 if ele  == '#' else 0
        if lock:
            locks.add(tuple(grid))
        else:
            keys.add(tuple(grid))

    locks = list(locks)
    keys = list(keys)
    fit = 0
    for lock in locks:
        for key in keys:
            res = [x+y for x, y in zip(key, lock)]
            if all(x <= r for x in res):
                fit += 1
    return fit 
                 
@execute
def p2(input):
    return None
 


def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/25_input.txt", 'r').read()
    example = open("2024/puzzle_input/25_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()

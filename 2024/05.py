import functools
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
    rules, order = input.split('\n\n')
    rules = rules.split('\n')
    order = order.split('\n')
    # brute force solution
    pairs = set()
    res = 0
    for rule in rules:
        n = rule.split('|')
        pairs.add(tuple(n))
    for cur in order:
        cur = cur.split(',')
        valid = True
        for i in range(len(cur)):
            for j  in range(i, len(cur)):
                if (cur[j], cur[i]) in pairs:
                   valid = False 
        if valid:
            res += int(cur[len(cur)//2])          
    return res
        
@execute
def p2(input):
    pairs, order = input.split('\n\n')
    pairs = pairs.split('\n')
    order = order.split('\n')
    # brute force solution
    rules = set()
    res = 0
    def custom_comparator(x, y):
        if (x, y) in rules:
            return -1
        elif (y, x) in rules:
            return 1
        else:
            return 0

    for pair in pairs:
        pair = pair.split("|")
        rules.add(tuple(pair))
    for update in order:
        update = update.split(',')
        sortedUpdate = sorted(update, key=functools.cmp_to_key(custom_comparator)) 
        if update != sortedUpdate:
            res += int(sortedUpdate[len(update)//2])
 
    return res 
 

def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/05_input.txt", 'r').read()
    example = open("2024/puzzle_input/05_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
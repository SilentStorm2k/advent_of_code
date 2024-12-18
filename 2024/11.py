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
    blinks = 25
    input = [int(ele) for ele in input.split()]
    for i in range(blinks):
        input = blink(input)
    return len(input) 
                 
@execute
def p2(input):
    blinks = 10 
    count = defaultdict(int)
    seen = set()
    input = [int(ele) for ele in input.split()]
    for i in range(blinks):
        print(i, len(input), " -> ", input)
        input = blink(input)
        # input = optimizedBlink(input, count, seen)
    return len(input) 
 
def blink (input):
    def evolve (stone):
        r1, r2 = 0, -1 
        s = str(stone)
        if stone == 0:
            r1 = 1
        elif len(s)%2 == 0:
            r1 = int(s[0:len(s)//2])
            r2 = int(s[len(s)//2:])
        else:
            r1 = stone*2024
        return r1, r2 
    stones = []
    for stone in input:
        s1, s2 = evolve(stone)
        stones.append(s1)
        if s2 != -1:
            stones.append(s2)
        # stones += ' ' + s1 + ' ' + s2
    
    return stones

def optimizedBlink (input, count, seen):
    def evolve (stone):
        r1, r2 = 0, -1 
        s = str(stone)
        if stone == 0:
            r1 = 1
        elif len(s)%2 == 0:
            r1 = int(s[0:len(s)//2])
            r2 = int(s[len(s)//2:])
        else:
            r1 = stone*2024
        return r1, r2 
    stones = []
    for stone in input:
        s1, s2 = evolve(stone)
        if s1 in seen:
            count[s1] += 1
        else:
            seen.add(s1)
            stones.append(s1)
        if s2 != -1:
            if s2 in seen:
                count[s2] += 1
            else:
                seen.add(s2)
                stones.append(s2)
        # stones += ' ' + s1 + ' ' + s2
    
    return stones



def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/11_input.txt", 'r').read()
    example = open("2024/puzzle_input/11_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    # p2(input)

if __name__ == "__main__":
    main()
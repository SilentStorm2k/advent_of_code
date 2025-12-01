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
    # if need to reuse p1 w/o decorator use : p1.__original(input)
    wrapper.__original = func
    return wrapper


@execute
def p1(input):
    rotations = input.split('\n')
    curPos = 50
    res = 0
    MOD = 100
    for rotation in rotations:
        direction, magnitude = (-1 if rotation[0]
                                == 'L' else 1), int(rotation[1:])
        curPos += direction*magnitude
        res += 1 if curPos % MOD == 0 else 0
    return res


@execute
def p2(input):
    rotations = input.split('\n')
    curPos = 50
    res = 0
    MOD = 100
    for rotation in rotations:
        direction, magnitude = (-1 if rotation[0]
                                == 'L' else 1), int(rotation[1:])
        prevPos = curPos % 100
        curPos += direction*(magnitude % MOD)
        curPos = curPos % 100
        res += magnitude//MOD  # adding minimum crossings due to over rotation
        if ((curPos < prevPos and direction > 0) or (curPos > prevPos and direction < 0)) and curPos and prevPos:
            # checks only if it crosses 0 (when it does not start and end at 0 since this is accounted by part 1 solution)
            res += 1

    return res + p1.__original(input)


def main():
    # when called from ~/advent_of_code$
    input = open("2025/puzzle_input/01_input.txt", 'r').read()
    example = open("2025/puzzle_input/01_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)


if __name__ == "__main__":
    main()

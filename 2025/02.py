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
    ranges = [range.split('-') for range in input.split(',')]
    count = 0
    for curRange in ranges:
        start, end = int(curRange[0]), int(curRange[1])
        for num in range(start, end + 1):
            cur = str(num)
            curLen = len(cur)//2
            if cur[:curLen] == cur[curLen:]:
                count += num

    return count


@execute
def p2(input):
    ranges = [range.split('-') for range in input.split(',')]
    count = 0
    for curRange in ranges:
        start, end = int(curRange[0]), int(curRange[1])
        for num in range(start, end + 1):
            cur = str(num)
            valid = False
            for repeatingLength in range(1, len(cur)//2 + 1):
                curValid = True
                for i in range(repeatingLength, len(cur)):
                    if cur[i] != cur[i-repeatingLength]:
                        curValid = False
                        break
                if curValid and len(cur) % repeatingLength == 0:
                    valid = True
                    break

            count += num if valid else 0

    return count


def main():
    # when called from ~/advent_of_code$
    input = open("2025/puzzle_input/02_input.txt", 'r').read()
    example = open("2025/puzzle_input/02_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)


if __name__ == "__main__":
    main()

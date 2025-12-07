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
def p1(input, debug=False):
    input = input.split('\n')
    prev = list(input[0])
    splitCount = 0
    for i in range(1, len(input)):
        cur = list(input[i])
        for j in range(len(prev)):
            if prev[j] == '|' or prev[j] == 'S':
                if cur[j] == '^':
                    splitCount += 1
                    if j-1 >= 0 and cur[j-1] == '.':
                        cur[j-1] = '|'
                    if j+1 <= len(cur) and cur[j+1] == '.':
                        cur[j+1] = '|'
                else:
                    cur[j] = '|'
        if debug:
            print(''.join(prev))
        prev = cur

    return splitCount


@execute
def p2(input):
    input = input.split('\n')
    prev = list(input[0])
    timelineCounts = defaultdict(int)
    for idx, ele in enumerate(prev):
        if ele == 'S':
            timelineCounts[(0, idx)] += 1
    timelines = 0
    for i in range(1, len(input)):
        cur = list(input[i])
        splitCount = 0
        for j in range(len(prev)):
            if prev[j] == '|' or prev[j] == 'S':
                if cur[j] == '^':
                    splitCount += 1
                    timelineCounts[(i, j-1)
                                   ] += max(timelineCounts[(i-1, j)], 1)
                    timelineCounts[(i, j+1)
                                   ] += max(timelineCounts[(i-1, j)], 1)
                    if j-1 >= 0 and cur[j-1] == '.':
                        cur[j-1] = '|'
                    if j+1 <= len(cur) and cur[j+1] == '.':
                        cur[j+1] = '|'
                else:
                    cur[j] = '|'
                    timelineCounts[(i, j)] += timelineCounts[(i-1, j)]

        prev = cur

    lastRow = len(input)-1
    for idx, beam in enumerate(prev):
        timelines += timelineCounts[(lastRow, idx)]

    return timelines


def main():
    # when called from ~/advent_of_code$
    input = open("2025/puzzle_input/07_input.txt", 'r').read()
    example = open("2025/puzzle_input/07_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example, True)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)


if __name__ == "__main__":
    main()

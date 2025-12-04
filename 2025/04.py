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
    # this is just a simple kernel/mask 3x3 for each position
    grid = [list(row) for row in input.split('\n')]
    R, C = len(grid), len(grid[0])
    forkLiftAccessible = 0
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '@' and kernel(grid, i, j) < 4:
                forkLiftAccessible += 1

    return forkLiftAccessible


@execute
def p2(input):
    grid = [list(row) for row in input.split('\n')]
    R, C = len(grid), len(grid[0])
    rollPositions = set()
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '@':
                rollPositions.add((i, j))

    forkLiftAccessible = 0
    iterate = True
    while iterate:
        iterate = False
        for roll in list(rollPositions):
            i, j = roll
            if kernel(grid, i, j) < 4:
                grid[i][j] = '.'
                rollPositions.remove(roll)
                forkLiftAccessible += 1
                iterate = True
    return forkLiftAccessible


def kernel(grid, r, c):
    R, C = len(grid), len(grid[0])
    count = 0
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if 0 <= i < R and 0 <= j < C and grid[i][j] == '@' and ((i, j) != (r, c)):
                count += 1
    return count


def main():
    # when called from ~/advent_of_code$
    input = open("2025/puzzle_input/04_input.txt", 'r').read()
    example = open("2025/puzzle_input/04_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)


if __name__ == "__main__":
    main()

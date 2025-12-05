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


def processInput(input):
    ranges, ingredients = input.split('\n\n')
    ranges = ranges.split('\n')
    ingredients = [int(i) for i in ingredients.split('\n')]
    ranges = sorted(
        list(map(lambda r: [int(s) for s in r.split('-')], ranges)))
    combinedRanges = [ranges[0]]
    for curRange in ranges:
        s, e = curRange
        if s <= combinedRanges[-1][1]:
            combinedRanges[-1][1] = max(combinedRanges[-1][1], e)
        else:
            combinedRanges.append(curRange)
    return combinedRanges, ingredients


@execute
def p1(input):
    ranges, ingredients = processInput(input)
    fresh = 0
    # brute force checking
    # can do binary search but why bother?
    for ingredient in ingredients:
        for curRange in ranges:
            s, e = curRange
            if s <= ingredient <= e:
                fresh += 1
                break
    return fresh


@execute
def p2(input):
    ranges, ingredients = processInput(input)
    fresh = 0
    for curRange in ranges:
        s, e = curRange
        fresh += e-s+1

    return fresh


def main():
    # when called from ~/advent_of_code$
    input = open("2025/puzzle_input/05_input.txt", 'r').read()
    example = open("2025/puzzle_input/05_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)


if __name__ == "__main__":
    main()

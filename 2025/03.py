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
    banks = input.split('\n')
    outputJoltage = 0
    for bank in banks:
        maxJoltage = 0
        largestJoltageSeen = 0
        jolts = [int(jolt) for jolt in bank]
        for curBatteryJoltage in jolts:
            curJoltage = largestJoltageSeen*10 + curBatteryJoltage
            maxJoltage = max(maxJoltage, curJoltage)
            largestJoltageSeen = max(largestJoltageSeen, curBatteryJoltage)
        outputJoltage += maxJoltage

    return outputJoltage


@execute
def p2(input):
    banks = input.split('\n')
    # bf is having 12 loops which is stupid n^12,
    # need a quadratic solution for this
    # other approach is to either pick a number or skip it and do calculation at the end
    # this is 2^n, I dont think there is appropriate memoization for this (since the states seem to be mostly unique)

    outputJoltage = 0
    for i, bank in enumerate(banks):
        cur = maxJoltage(bank, 12)
        outputJoltage += cur

    return outputJoltage


def maxJoltage(homeBank, digits):
    # taking greedy approach, deleting smaller characters until we reach our size
    bank = list(homeBank)
    while len(bank) > digits:
        flag = False
        for i in range(1, len(bank)):
            if bank[i] > bank[i-1]:
                del bank[i-1]
                flag = True
                break
        if not flag:
            del bank[len(bank)-1]
    return int(''.join(bank))


def main():
    # when called from ~/advent_of_code$
    input = open("2025/puzzle_input/03_input.txt", 'r').read()
    example = open("2025/puzzle_input/03_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)


if __name__ == "__main__":
    main()

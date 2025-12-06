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
    lines = input.split('\n')
    lines = [line.split() for line in lines]
    probs, ops = lines[:-1], lines[-1]
    total = 0
    for idx, op in enumerate(ops):
        curAns = 0 if (op == '+' or op == '-') else 1
        for row in range(len(probs)):
            if op == '+':
                curAns += int(probs[row][idx])
            elif op == '-':
                curAns -= int(probs[row][idx])
            elif op == '*':
                curAns *= int(probs[row][idx])
            elif op == '/':
                curAns /= int(probs[row][idx])
        total += curAns

    return total


@execute
def p2(input):
    nums = []
    lines = input.split('\n')
    longest = 0
    for line in lines:
        longest = max(longest, len(line))
    ops = lines[-1]
    total = 0
    skip = False
    for col in range(longest-1, -1, -1):
        if skip:
            skip = False
            continue
        num = ''
        for row in range(len(lines)-1):
            num += lines[row][col]
        nums.append(num)
        curOp = ops[col] if col < len(ops) else ' '
        if curOp != ' ':
            eval = 0 if (curOp == '+') else 1
            for n in nums:
                if curOp == '+':
                    eval += int(n)
                if curOp == '*':
                    eval *= int(n)
            total += eval
            nums = []
            skip = True

    return total


def main():
    # when called from ~/advent_of_code$
    input = open("2025/puzzle_input/06_input.txt", 'r').read()
    example = open("2025/puzzle_input/06_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)


if __name__ == "__main__":
    main()

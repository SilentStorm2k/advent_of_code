import time
import functools
import regex as re

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
    input = input.split('\n')
    ways = 0
    for line in input:
        dots, blocks = line.split()
        blocks = [int(x) for x in blocks.split(',')]
        memo.clear()
        ans = f(dots, blocks, 0, 0, 0)
        ways += ans

    return ways

@execute
def p2(input):
    input = input.split('\n')
    ways = 0
    for line in input:
        dots, blocks = line.split()
        blocks = [int(x) for x in blocks.split(',')]
        memo.clear()
        dots = '?'.join([dots, dots, dots, dots, dots])
        blocks = blocks*5
        # print(f'{dots} {blocks}')
        ways += f(dots, blocks, 0, 0, 0)

    return ways

memo = {}
def f(dots, blocks, i, bi, current):
    key = (i, bi, current)
    if key in memo:
        return memo[key]
    if i == len(dots):
        if bi == len(blocks) and current == 0:
            return 1
        elif bi == len(blocks)-1 and blocks[bi]==current:
            return 1
        else:
            return 0
    ans = 0
    for c in ['.', '#']:
        if dots[i] == c or dots[i] == '?':
            if c == '.' and current == 0:
                ans += f(dots, blocks, i+1, bi, 0)
            elif c == '.' and current > 0 and bi<len(blocks) and blocks[bi]==current:
                ans += f(dots, blocks, i+1, bi+1, 0)
            elif c == '#':
                ans += f(dots, blocks, i+1, bi, current+1)
    memo[key] = ans
    return ans


# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 12/puzzle_input/example.txt" if ex else "2023/day 12/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
import time
import re

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
    wf, parts = input.split('\n\n')
    wf = [f for f in wf.split()]
    parts = [re.findall(r'[0-9]+', p) for p in parts.split()]
    wf = {f.split('{')[0] : f.split(r'{')[1][:-1].split(',') for f in wf}
    ans = 0
    # iterating over all parts
    for p in parts:
        cur_wf = 'in'
        # starting at workflow 'in' execute the current part until its accepted or rejected
        while cur_wf != 'A' and cur_wf != 'R':
            # getting next workflow using f
            cur_wf = f(wf.get(cur_wf), p)
        # if part was accepted, add xmas value to answer
        if cur_wf == 'A':
            ans += sum(map(int, p))
    return ans



@execute
def p2(input):
    wf = input.split('\n\n')[0]
    wf = {f.split('{')[0] : f.split(r'{')[1][:-1].split(',') for f in wf.split()}
    # creating the maximum possible values for x,m,a,s (1-4000) and storing them in dict
    ranges = {key: (1,4000) for key in 'xmas'}
    # counting all possible admissible ranges
    sum = count(ranges, wf)
    return sum

# counting all possible ranges of values for which start at wf 'in'
def count(ranges, wf, cur_wf = 'in'):
    # if rejected nothing to check
    if cur_wf == 'R': 
        return 0
    # if accepted, get number of possible ways to achieve this from the possible ranges
    if cur_wf == 'A':
        prod = 1
        for lo, hi in ranges.values():
            prod *= hi-lo+1
        return prod
    
    conds = wf.get(cur_wf)
    total = 0
    # evaluating all the conditions
    for c in conds:
        # when the fall back condition is achieved, get its count with the current admissible ranges
        if not re.search(':', c):
            total += count(ranges, wf, c)
            break

        cond, ret = c.split(':')
        key, cmp, val = cond[0], cond[1], int(cond[2:])
        lo, hi = ranges[key]
        # if the comparison is '<', add the ranges which satisfy (valid = v) and do not satisfy this (invalid = inv)
        if cmp == '<':
            v = (lo, val-1)
            inv = (val, hi)
        # similar for '>'
        else:
            v = (val+1, hi)
            inv = (lo, val)
        
        # when the ranges are valid, and current condition is true, expand this leaf (at ret)
        if v[0] <= v[1]:
            copy = dict(ranges)
            copy[key] = v
            total += count(copy, wf, ret)
        
        # when the ranges are valid and the current condition is not true, modify the ranges for when next condition is evaluated in for loop
        if inv[0] <= inv[1]:
            ranges = dict(ranges)
            ranges[key] = inv
        else:
            break
    return total

# given conditions and parts, evaluate condition on part
def f(conds, parts):
    x, m, a, s = parts
    x, m, a, s = int(x), int(m), int(a), int(s)
    for c in conds:
        # if condition is the fallback value, return it
        if not re.search(':', c):
            return c
        cond, ret = c.split(':')
        # if evaluation of the current condition is true, return the ret value
        if eval(cond):
            return ret
    assert False

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 19/puzzle_input/example.txt" if ex else "2023/day 19/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
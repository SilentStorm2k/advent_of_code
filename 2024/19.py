from functools import lru_cache
import time
import re
from collections import defaultdict, deque
import heapq
from typing import List

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
    towels, patterns = input.split('\n\n')
    towels = [towel.strip() for towel in towels.split(',')]
    patterns = patterns.split('\n')
    towels = frozenset(towels)
    res = 0
    for pattern in patterns:
        if canMakeSentence(pattern, towels):
            res += 1
            
    return res 
                 
count = 0
@execute
def p2(input):
    towels, patterns = input.split('\n\n')
    towels = [towel.strip() for towel in towels.split(',')]
    patterns = patterns.split('\n')
    towels = frozenset(towels)
    res = 0
    for i, pattern in enumerate(patterns):
        # sentencesMade(pattern, towels, [], results, 0)
        ans = canMakeSentence(pattern, towels, p2=True)
        print(i, ans)
        res += ans
            
    return res 
 
@lru_cache()
def canMakeSentence (sentence: str, wordList: frozenset, p2=False):
    q = deque([0])
    seen = set()
    L = len(sentence)
    res = 0
    while q:
        start = q.popleft()
        if start == L:
            res += 1
            if not p2:
                return res
            continue
        for end in range(start + 1, L+1):
            if end in seen and not p2:
                continue
            if sentence[start:end] in wordList:
                q.append(end)
                seen.add(end)
    return res 
    

def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/19_input.txt", 'r').read()
    example = open("2024/puzzle_input/19_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
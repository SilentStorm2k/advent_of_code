import time
from collections import defaultdict, deque
import heapq

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
    safeCount = 0
    for line in input:
        levels = [int(level) for level in line.split()]
        safeCount += isLineValid(levels)
    return safeCount
 
    
@execute
def p2(input):
    input = input.split('\n')
    safeCount = 0
    for line in input:
        levels = [int(level) for level in line.split()]
        for i in range(len(levels)):
            if isLineValid(levels, i):
                safeCount += 1
                break
    return safeCount
        
def isLineValid (line, skip = -1):
    left = line[:skip]
    right = line[skip+1:]
    if skip == -1:
        left = []
        right = line
    asc = isAsc(left) and isAsc(right)
    desc = isDesc(left) and isDesc(right)
    safe = isSafe(left) and isSafe(right)
    if left and right:
        asc = asc and left[-1] < right[0]
        desc = desc and left[-1] > right[0]
        safe = safe and 1 <= abs(left[-1]-right[0]) <= 3
    return 1 if (asc or desc) and safe else 0

def isAsc (arr):
    if not arr:
        return True
    pre = arr[0]
    for i in range(1, len(arr)):
        if pre >= arr[i]:
            return False
        pre = arr[i]
    return True

def isDesc (arr):
    if not arr:
        return True
    pre = arr[0]
    for i in range(1, len(arr)):
        if pre <= arr[i]:
            return False
        pre = arr[i]
    return True

def isSafe (arr):
    if not arr:
        return True
    pre = arr[0]
    for i in range(1, len(arr)):
        if not (1 <= abs(pre - arr[i]) <= 3):
            return False
        pre = arr[i]
    return True




def main():
    # when called from ~/Code/repos/advent_of_code$
    input = open("2024/puzzle_input/02_input.txt", 'r').read()
    example = open("2024/puzzle_input/02_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
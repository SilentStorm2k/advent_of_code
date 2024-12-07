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
    wrapper.__original = func # if need to reuse p1 w/o decorator use : p1.__original(input)
    return wrapper 


@execute
def p1(input):
    input = input.split('\n')
    res = 0
    for line in input:
        val, nums = line.split(':')
        val = int(val)
        nums = [int(n) for n in nums.split(' ')[1:]]
        l = [nums[0]]
        for i in range(1, len(nums)):
            lPrime = set() 
            for num in l:
                lPrime.add(num+nums[i])
                lPrime.add(num*nums[i])
            if i == len(nums)-1:
                l = lPrime
            else:
                l = list(lPrime)
        res += val if val in l else 0
    return res 
                 
@execute
def p2(input):
    input = input.split('\n')
    res = 0
    for line in input:
        val, nums = line.split(':')
        val = int(val)
        nums = [int(n) for n in nums.split(' ')[1:]]
        l = [nums[0]]
        for i in range(1, len(nums)):
            lPrime = set() 
            for num in l:
                lPrime.add(num+nums[i])
                lPrime.add(num*nums[i])
                lPrime.add(int(str(num)+str(nums[i])))
            if i == len(nums)-1:
                l = lPrime
            else:
                l = list(lPrime)
        res += val if val in l else 0
    return res 


def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/07_input.txt", 'r').read()
    example = open("2024/puzzle_input/07_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
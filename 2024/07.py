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
def p1(input, p2 = False):
    input = input.split('\n')
    res = 0
    for line in input:
        val, nums = line.split(':')
        val = int(val)
        nums = [int(n) for n in nums.split(' ')[1:]]
        possibilities = {nums[0]}
        for i in range(1, len(nums)):
            resAfterOperation = set() 
            for num in list(possibilities):
                add = num+nums[i]
                mul = num*nums[i] 
                cat = int(str(num)+str(nums[i]))
                if add <= val:
                    resAfterOperation.add(add)
                if mul <= val:
                    resAfterOperation.add(mul)
                if cat <= val and p2:
                    resAfterOperation.add(cat)
            possibilities = resAfterOperation
        res += val if val in possibilities else 0
    return res 
                 
@execute
def p2(input):
    return p1.__original(input, True)


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
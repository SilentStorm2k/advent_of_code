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
    MOD = 16777216
    cache = {}
    def generateSecret (secret):
        if secret in cache:
            return cache[secret] 
        key = secret
        tmp = secret*64
        secret = (secret ^ tmp) % MOD
        tmp = secret//32
        secret = (secret ^ tmp) % MOD
        tmp = secret*2048
        secret = (secret ^ tmp) % MOD
        cache[key] = secret
        return secret
    
    res = 0
    for secret in input.split('\n'):
        secret = int(secret)
        for i in range(2000):
            secret = generateSecret(secret)
        res += secret
    print(len(cache))

    return res 
                 
@execute
def p2(input):
    return None
    
 


def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/22_input.txt", 'r').read()
    example = open("2024/puzzle_input/22_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
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
    res = 0
    for secret in input.split('\n'):
        secret = int(secret)
        res += generateSecrets(secret)[-1]
    return res 
                 
@execute
def p2(input):
    allSeq = defaultdict(int) 
    for secret in input.split('\n'):
        secretList = generateSecrets(int(secret))
        secretList = [ele%10 for ele in secretList]
        seq = generateSequences (secretList) 
        for key, val in seq.items():
            allSeq[key] += val
    return max(allSeq.values())
    
def generateSecrets (secret, length = 2000):
    secrets = [secret]
    for _ in range(length):
        secret = prune(mix(secret, secret*64))
        secret = prune(mix(secret, secret//32))
        secret = prune(mix(secret, secret*2048))
        secrets.append(secret)
    return secrets

def prune (secret):
    return secret % 16777216

def mix (s1, s2):
    return s1 ^ s2

def generateSequences (secrets):
    seq = defaultdict(int) 
    start = tuple([secrets[j]-secrets[j-1] for j in range(1, 5)])
    a, b, c, d = start
    for i in range(5, len(secrets)):
        a = b
        b = c
        c = d
        d = secrets[i]-secrets[i-1]
        curSeq = (a,b,c,d)
        if curSeq not in seq:
            seq[curSeq] = secrets[i]
    return seq

def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/22_input.txt", 'r').read()
    example = open("2024/puzzle_input/22_example.txt", 'r').read()
    example2 = open("2024/puzzle_input/22_example2.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example2)
    p2(input)

if __name__ == "__main__":
    main()
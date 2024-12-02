import time
import sys
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
    l1, l2 = [], []
    for line in input:
        line = line.split('  ')
        a = int(line[0])
        b = int(line[1])
        heapq.heappush(l1, a)
        heapq.heappush(l2, b)
    
    dist = 0 
    for _ in range(len(l1)):
        s1, s2 = heapq.heappop(l1), heapq.heappop(l2)
        dist += abs(s1-s2)
    return dist

    
@execute
def p2(input):
    input = input.split('\n')
    l1 = []
    l2 = defaultdict(int)
    for line in input:
        line = line.split('  ')
        a, b = line 
        a, b = int(a), int(b)
        l1.append(a)
        l2[b] += 1
    
    sol = 0
    for num in l1:
        sol += num*l2[num]
        
    return sol
        

def main():
    # when called from ~/Code/repos/advent_of_code$
    input = open("2024/puzzle_input/01_input.txt", 'r').read()
    example = open("2024/puzzle_input/01_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
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
    s = []
    for i in range(len(input)):
        if i%2==0:
            for j in range(int(input[i])):
                s.append(i//2)
        else:
            for j in range(int(input[i])):
                s.append('.')
            
    end = len(s)-1
    for i in range(len(s)):
        while end >= 0 and s[end] == '.':
            end -= 1
        if end <= i:
            break
        if s[i] == '.':
            s[i], s[end] = s[end], s[i]
    
    res = 0
    for i in range(len(s)):
        if s[i] == '.':
            break
        res += s[i]*i
    return res 
                 
@execute
def p2(input):
    files, gaps = [], []
    curIdx = 0
    for i in range(len(input)):
        if i%2==0:
            files.append((int(input[i]), curIdx, i//2))
        else:
            gaps.append((int(input[i]), curIdx))
        curIdx += int(input[i])
    
    for i in range(len(files)-1,-1,-1):
        fLen, fIdx, c = files[i]
        gLen, gIdx = gaps[0]
        for j in range(len(gaps)):
            gLen, gIdx = gaps[j]
            if gIdx > fIdx:
                break
            if gLen >= fLen: 
                files.append((fLen, gIdx, c))
                # res += i*fLen*(2*gIdx+fLen-1)/2
                gaps[j] = (gLen-fLen, gIdx+fLen)
                gaps.append((fLen, fIdx))
                break

    s = []
    for i in range(len(input)):
        if i%2==0:
            for j in range(int(input[i])):
                s.append(i//2)
        else:
            for j in range(int(input[i])):
                s.append('.')
     
    for l, idx, cost in files:
        for j in range(l):
            s[idx+j] = cost
    for l, idx in gaps:
        for j in range(l):
            s[idx+j] = '.'
    s = [str(ele) for ele in s]
    return getScore(s)
 
def getScore (s):
    res = 0
    for i in range(len(s)):
        res += i*int(s[i]) if s[i] != '.' else 0
    return res

def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/09_input.txt", 'r').read()
    example = open("2024/puzzle_input/09_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
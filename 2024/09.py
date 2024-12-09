import time
import re
from collections import OrderedDict, defaultdict, deque
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
            # swapping with earliest free space
            s[i], s[end] = s[end], s[i]
    
    res = 0
    for i in range(len(s)):
        if s[i] == '.':
            break
        res += s[i]*i
    return res 
                 
@execute
def p2(input):
    files = defaultdict(tuple) # each element is of #fileNumber : (#fileLength, #startIdx)
    gaps  = [] # each element is of (#gapLength,  #gapStartIdx)
    curIdx = 0
    lastFile = 0
    for i in range(len(input)):
        if i%2==0:
            files[i//2] = (int(input[i]), curIdx)
            lastFile = i//2
        else:
            gaps.append((int(input[i]), curIdx))
        curIdx += int(input[i])
    
    for fNum in range(lastFile, -1, -1):
        fLen, fIdx = files[fNum]
        gLen, gIdx = gaps[0]
        for j in range(len(gaps)):
            gLen, gIdx = gaps[j]
            if gIdx > fIdx:
                # gap appearing after fileLocation (i.e cant move it upwards)
                break
            if gLen >= fLen: 
                # moving file forward 
                files[fNum] = (fLen, gIdx)
                gaps[j] = (gLen-fLen, gIdx+fLen)
                break
    return getScore(files)
 
def getScore(files):
    res = 0
    for fNum, fVal in files.items():
        fLen, fIdx = fVal
        res += fNum*fLen*(fIdx+fIdx+fLen-1)//2
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
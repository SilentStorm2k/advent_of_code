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
def p1(input, p2=False):
    antennas = defaultdict(list)
    antinodes = set()
    m, n = len(input.split('\n')), len(input.split('\n')[0])

    for row, line in enumerate(input.split('\n')):
        for col, ele in enumerate(line):
            if ele == '.':
                continue
            antennas[ele].append((row, col)) 
            
    for antenna_type, antenna_locs in antennas.items():
        # go through every pair in antenna_locs:
        for i in range(len(antenna_locs)):
            for j in range(i+1, len(antenna_locs)):
                r1, c1 = antenna_locs[i]
                r2, c2 = antenna_locs[j]    
                dr, dc = r2-r1, c2-c1
                curR, curC = r2+dr, c2+dc

                while 0 <= curR < m and 0 <= curC < n:
                    antinodes.add((curR, curC))
                    curR, curC = curR+dr, curC+dc
                    if not p2:
                        break
                    
                curR, curC = r1-dr, c1-dc
                while 0 <= curR < m and 0 <= curC < n:
                    antinodes.add((curR, curC))
                    curR, curC = curR-dr, curC-dc
                    if not p2:
                        break
                    
                if p2:
                    antinodes.add(antenna_locs[i])
                    antinodes.add(antenna_locs[j])

    return len(antinodes)
                 
@execute
def p2(input):
    return p1.__original(input, True)


def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/08_input.txt", 'r').read()
    example = open("2024/puzzle_input/08_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
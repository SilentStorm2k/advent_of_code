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

defaultMasks = [
    [['X', 'M', 'A', 'S']],
    [['S', 'A', 'M', 'X']],
    [['X'], ['M'], ['A'], ['S']],
    [['S'], ['A'], ['M'], ['X']],
    [['X', '.', '.', '.'], ['.', 'M', '.', '.'], ['.', '.', 'A', '.'], ['.', '.', '.', 'S']],
    [['.', '.', '.', 'X'], ['.', '.', 'M', '.'], ['.', 'A', '.', '.'], ['S', '.', '.', '.']],
    [['S', '.', '.', '.'], ['.', 'A', '.', '.'], ['.', '.', 'M', '.'], ['.', '.', '.', 'X']],
    [['.', '.', '.', 'S'], ['.', '.', 'A', '.'], ['.', 'M', '.', '.'], ['X', '.', '.', '.']],
]

@execute
def p1(input, masks = defaultMasks):
    grid = []
    for line in input.split('\n'):
        grid.append([ele for ele in list(line)]) 
    m, n = len(grid), len(grid[0])
    count = 0
    for i in range(m):
        for j in range(n):
            for mask in masks:
                count += evaluateMask(grid, i, j, mask)
    return count 
                 
@execute
def p2(input):
    masks = [
        [['M', '.', 'S'], ['.', 'A', '.'], ['M', '.', 'S']],
        [['S', '.', 'S'], ['.', 'A', '.'], ['M', '.', 'M']],
        [['S', '.', 'M'], ['.', 'A', '.'], ['S', '.', 'M']],
        [['M', '.', 'M'], ['.', 'A', '.'], ['S', '.', 'S']],
    ]
    return p1.__original(input, masks) 
 
def evaluateMask (grid, i, j, mask):
    m, n = len(grid), len(grid[0])
    for r in range(len(mask)):
        for c in range(len(mask[0])):
            if mask[r][c] == '.':
                continue
            if not (0 <= i+r < m and 0 <= j+c < n):
                return 0 
            if mask[r][c] != grid[i+r][j+c]:
                return 0
    return 1
    
def main():
    # when called from ~/Code/repos/advent_of_code$
    input = open("2024/puzzle_input/04_input.txt", 'r').read()
    example = open("2024/puzzle_input/04_example.txt", 'r').read()
    example2 = open("2024/puzzle_input/04_example2.txt", 'r').read()
    example3 = open("2024/puzzle_input/04_example3.txt", 'r').read()
    example4 = open("2024/puzzle_input/04_example4.txt", 'r').read()
    example5 = open("2024/puzzle_input/04_example5.txt", 'r').read()

    print("\nPart 1:")
    # p1(example)
    # p1(example2)
    # p1(example3)
    p1(input)
    print("\nPart 2:")
    # p2(example)
    # p2(example4)
    # p2(example5)
    p2(input)

if __name__ == "__main__":
    main()
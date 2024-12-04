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
    grid = []
    for line in input.split('\n'):
        grid.append([ele for ele in list(line)]) 
    m, n = len(grid), len(grid[0])
    count = 0
    masks = [
        [['X', 'M', 'A', 'S']],
        [['S', 'A', 'M', 'X']],
        [['X'], ['M'], ['A'], ['S']],
        [['S'], ['A'], ['M'], ['X']],
        [['X', '.', '.', '.'], ['.', 'M', '.', '.'], ['.', '.', 'A', '.'], ['.', '.', '.', 'S']],
        [['.', '.', '.', 'X'], ['.', '.', 'M', '.'], ['.', 'A', '.', '.'], ['S', '.', '.', '.']],
        [['S', '.', '.', '.'], ['.', 'A', '.', '.'], ['.', '.', 'M', '.'], ['.', '.', '.', 'X']],
        [['.', '.', '.', 'S'], ['.', '.', 'A', '.'], ['.', 'M', '.', '.'], ['X', '.', '.', '.']],
    ]
    for i in range(m):
        for j in range(n):
            flag = False
            if i == 3 and j == 6:
                for r in range(4):
                    s = ''
                    for c in range(4):
                        s += grid[i+r][j+c]
            for mask in masks:
                count += findMask(grid, i, j, mask)
    return count 
    # grid = []
    # for line in input.split('\n'):
    #     grid.append([ele for ele in list(line)]) 
    # m, n = len(grid), len(grid[0])
    # count = 0
    # for i in range(m):
    #     for j in range(n):
    #         if isSpecialWord(grid, i, j) > 0:
    #             print(i, j, " - ", (count+isSpecialWord(grid, i, j)))
    #         count += isSpecialWord(grid, i, j)
    # return count 
                 
@execute
def p2(input):
    grid = []
    for line in input.split('\n'):
        grid.append([ele for ele in list(line)]) 
    m, n = len(grid), len(grid[0])
    count = 0
    masks = [
        [['M', '.', 'S'], ['.', 'A', '.'], ['M', '.', 'S']],
        [['S', '.', 'S'], ['.', 'A', '.'], ['M', '.', 'M']],
        [['S', '.', 'M'], ['.', 'A', '.'], ['S', '.', 'M']],
        [['M', '.', 'M'], ['.', 'A', '.'], ['S', '.', 'S']]
    ]
    for i in range(m):
        for j in range(n):
            for mask in masks:
                count += findMask(grid, i, j, mask)
    return count 
 
def isSpecialWord(grid, i, j):
    if grid[i][j] != 'X':
       return 0
    m, n = len(grid), len(grid[0])
    seq = ["" for i in range(8)]
    seq[0]  = grid[i][j] + grid[i-1][j] + grid[i-2][j] + grid[i-3][j]       if 0 <= i-3 < m and 0 <= j < n   else "" 
    seq[1]  = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j]       if 0 <= i+3 < m and 0 <= j < n   else "" 
    seq[2]  = grid[i][j] + grid[i][j-1] + grid[i][j-2] + grid[i][j-3]       if 0 <= i < m and 0 <= j-3 < n   else "" 
    seq[3]  = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i][j+3]       if 0 <= i < m and 0 <= j+3 < n   else "" 
    seq[4]  = grid[i][j] + grid[i-1][j-1] + grid[i-2][j-2] + grid[i-3][j-3] if 0 <= i-3 < m and 0 <= j-3 < n else "" 
    seq[5]  = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3] if 0 <= i+3 < m and 0 <= j+3 < n else "" 
    seq[6]  = grid[i][j] + grid[i-1][j+1] + grid[i-2][j+2] + grid[i-3][j+3] if 0 <= i-3 < m and 0 <= j+3 < n else "" 
    seq[7]  = grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] + grid[i+3][j-3] if 0 <= i+3 < m and 0 <= j-3 < n else "" 

    count = 0
    for word in seq:
        if word == "XMAS":
            count += 1
    return count 

def findMask (grid, i, j, mask):
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
    p1(example)
    p1(example2)
    p1(example3)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(example4)
    p2(example5)
    p2(input)

if __name__ == "__main__":
    main()
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
    for row in input.split('\n'):
        grid.append(list(row))
    seen = set()
    curSeen = set()
    perimeter = 0
    m, n = len(grid), len(grid[0])
    d = [(0,1), (1,0), (0,-1), (-1,0)]
    def dfs (i, j, region):
        nonlocal perimeter
        if  not (0 <= i < m and 0 <= j < n) or \
            grid[i][j] != region:
            perimeter += 1
            return
        if  (i,j) in seen or (i,j) in curSeen: 
            return
        seen.add((i,j))
        curSeen.add((i,j))
        for di, dj in d:
            dfs (i+di, j+dj, region)
    
    res = 0
    for i in range(m):
        for j in range(n):
            curSeen = set()
            perimeter = 0
            dfs (i, j, grid[i][j])
            if curSeen:
                # print("A region of", grid[i][j], "plants with price", len(curSeen), "*", perimeter, "=", (len(curSeen)*perimeter))
                res += len(curSeen)*perimeter
                
    return res  
                 
@execute
def p2(input):
    grid = []
    for row in input.split('\n'):
        grid.append(list(row))
    seen = set()
    curSeen = set()
    corners = list()
    edges = defaultdict(int)
    m, n = len(grid), len(grid[0])
    d = [(0,1), (1,0), (0,-1), (-1,0)]
    def dfs (i, j, region):
        if  not (0 <= i < m and 0 <= j < n) or \
            grid[i][j] != region:
            edges[(i,j)] += 1
            return
        if  (i,j) in seen or (i,j) in curSeen: 
            return
        seen.add((i,j))
        curSeen.add((i,j))
        for _ in range(isCorner(i,j)):
        # if isCorner (i,j) > 0:
            corners.append((i,j)) 
        for di, dj in d:
            dfs (i+di, j+dj, region)
    
    def isCorner (i,j):
        d = [(1,1),(1,-1),(-1,1),(-1,-1)] 
        cornerCount = 0
        for di, dj in d:
            if 0<=i+di<m and 0<=j+dj<n:
                if grid[i][j] != grid[i+di][j+dj] and grid[i][j] == grid[i+di][j] and grid[i][j] == grid[i][j+dj]:
                    cornerCount += 1
                if grid[i][j] != grid[i+di][j] and grid[i][j] != grid[i][j+dj]:
                    cornerCount += 1
            else:
                if 0<=i+di<m and grid[i][j] != grid[i+di][j]:
                    cornerCount += 1
                if 0<=j+dj<n and grid[i][j] != grid[i][j+dj]:
                    cornerCount += 1
                if not (0<=i+di<m) and not (0<=j+dj<n):
                    cornerCount += 1
                
        return cornerCount
             
    
    def removeSides (k, l):
        dk, dl = 0, 0
        if (k+1,l) in edges or (k-1,l) in edges:
            # horizontal
            dk = 1
            dl = 0
        elif (k,l+1) in edges or (k, l-1) in edges:
            # vertical
            dk = 0
            dl = 1
        else:
            # lone island
            sides = edges[(k,l)]
            # print((k,l), sides)
            del edges[(k,l)]
            return sides
        # streak = deque()
        ck, cl = k, l
        while (k,l) in edges:
            assert edges[(k,l)] >= 1, f"Edge shouldnt exists: {(k,l)}"
            edges[(k,l)] -= 1
            if edges[(k,l)] <= 0:
                del edges[(k,l)]
            # streak.append((k,l))
            k += dk 
            l += dl
        k, l = ck-dk, cl-dl 
        while (k, l) in edges:
            assert edges[(k,l)] >= 1, f"Edge shouldnt exists: {(k,l)}"
            edges[(k,l)] -= 1
            if edges[(k,l)] <= 0:
                del edges[(k,l)]
            # streak.appendleft((k,l))
            k -= dk 
            l -= dl
        
        # print(streak)
        return 1

        
    res = 0
    for i in range(m):
        for j in range(n):
            curSeen = set()
            edges = defaultdict(int)
            corners = list()
            perimeter = 0
            dfs (i, j, grid[i][j])
            if curSeen:
                sides = 0
                perimeter = sum(edges.values()) 
                # while edges:
                #     for edge in list(edges):
                #         if edge in edges:
                #             k, l = edge
                #             sides += removeSides (k, l)
                # print("A region of", grid[i][j], "plants with price", len(curSeen), "*", sides, "=", (len(curSeen)*sides))
                # res += len(curSeen)*sides
                # print("A region of", grid[i][j], "plants with price", len(curSeen), "*", len(corners), "=", (len(curSeen)*len(corners)))
                # print(corners)
                #
                res += len(curSeen)*len(corners)
    return res  

def rotate_matrix(matrix):
    n = len(matrix)
    return [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]

def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/12_input.txt", 'r').read()
    example = open("2024/puzzle_input/12_example.txt", 'r').read()
    example2 = open("2024/puzzle_input/12_example2.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(example2)
    p2(input)

if __name__ == "__main__":
    main()
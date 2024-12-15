import time
import re
from collections import defaultdict, deque
import heapq

from matplotlib import animation, pyplot as plt

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
    dir = {
        '>': (0,1),
        '<': (0,-1),
        '^': (-1,0),
        'v': (1,0),
    }
    frames = []
    pos, instructions = input.split('\n\n')
    grid = []
    start = ()
    for i, row in enumerate(pos.split('\n')):
        grid.append(list(row))
        if '@' in row:
            start = (i, row.index('@'))
    instructions = instructions.replace('\n', '')
    def move ( direction ):
        nonlocal start, grid
        di, dj = dir[direction]
        si, sj = start
        i, j = start
        moved = False
        while grid[i+di][j+dj] != '#' and grid[i+di][j+dj] != '.':
            i += di
            j += dj
        while grid[i+di][j+dj] == '.' and not (i+di == si and j+dj == sj):
            grid[i][j], grid[i+di][j+dj] = grid[i+di][j+dj], grid[i][j]
            moved = True
            i -= di
            j -= dj
        if moved:
            start = (si+di, sj+dj)
            

    for d in instructions:
        move (d)
        # frames.append(toString(grid))
    
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O':
                res += 100*i + j
    
    # def update_plot(i, ax, frames):
    #     # Add text to display the frame number
    #     ax.clear()
    #     ax.text(0.5, 0.5, frames[i], ha='center', va='center', fontfamily = 'monospace')

    # print("Done")
    # fig, ax = plt.subplots()
    # ani = animation.FuncAnimation(fig, update_plot, frames=len(frames), fargs=(ax, frames), interval=10)
    # ani.save('2024/15_visualization.webm', writer='ffmpeg', codec='libvpx', bitrate=1000000)
    # plt.show()
    #
                
    return res 
                 
@execute
def p2(input):
    dir = {
        '>': (0,1),
        '<': (0,-1),
        '^': (-1,0),
        'v': (1,0),
    }
    pos, instructions = input.split('\n\n')
    grid = []
    start = ()
    for i, row in enumerate(pos.split('\n')):
        row = row.replace('.', '..').replace('#', '##').replace('O', '[]').replace('@', '@.')
        grid.append(list(row))
        if '@' in row:
            start = (i, row.index('@'))
    instructions = instructions.replace('\n', '')
    def move ( direction ):
        nonlocal start, grid
        di, dj = dir[direction]
        q = deque(tuple())
        q.append(start)
        seen = set()
        while q:
            ele = q.popleft()
            ci, cj = ele
            if (ci,cj) in seen:
                continue
            seen.add((ci,cj))
            if grid[ci][cj] == '#':
                return   
            elif grid[ci][cj] == '.':
                continue
            elif grid[ci][cj] == ']':
                q.append((ci, cj-1))    
            elif grid[ci][cj] == '[':
                q.append((ci, cj+1))
            q.append((ci+di, cj+dj))
        
        for locs in sorted(list(seen), key=lambda x: -x[0] if di == 1 else x[0] if di == -1 else -x[1] if dj == 1 else x[1]):
            ci, cj = locs
            if grid[ci][cj] == '.':
                continue
            grid[ci][cj], grid[ci+di][cj+dj] = grid[ci+di][cj+dj], grid[ci][cj]
            
        start = (start[0]+di, start[1]+dj)
            
    for d in instructions:
        move (d)
    
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '[':
                res += 100*i + j
    
    # print(toString(grid))
    return res 

def toString (g):
    s = ""
    for row in g:
        s += "".join(row) + '\n'
    return s


def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/15_input.txt", 'r').read()
    example = open("2024/puzzle_input/15_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
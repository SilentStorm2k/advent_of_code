import functools
import time
import re
from collections import defaultdict, deque
import heapq
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def execute(func):
    def wrapper(*args):   
        t1 = time.time()
        print(f'Answer for {func.__name__} : {func(*args)}')
        t2 = time.time()
        print(f'Executed in : {round(t2-t1, 5)}')
    wrapper.__original = func # if need to reuse p1 w/o decorator use : p1.__original(input)
    return wrapper 


@execute
def p1(input, m=101, n=103):
    iterations = 100
    robots = [robot for robot in input.split('\n')]
    for i in range(len(robots)):
        robot = robots[i]
        robot = robot.split('=')[1:]
        robot = [r.split(' ')[0].split(',') for r in robot]
        robot = [int(r) for s in robot for r in s]
        robots[i] = tuple(robot)

    def simulateRobot (robot):
        x, y, dx, dy = robot
        return ((x+dx)%m, (y+dy)%n, dx, dy)
    
    for i in range(iterations):
        for j in range(len(robots)):
            robots[j] = simulateRobot(robots[j]) 
    
    tr, tl, br, bl = 0, 0, 0, 0
    for robot in robots:
        x, y, _, __ = robot
        if x < m//2 and y < n//2:
            tl += 1
        if x < m//2 and y > n//2:
            bl += 1
        if x > m//2 and y < n//2:
            tr += 1
        if x > m//2 and y > n//2:
            br += 1

    return tr*tl*br*bl 
                 
@execute
def p2(input, m=101, n=103):
    iterations = 10000 
    frames = []
    frameNum = []
    robots = [robot for robot in input.split('\n')]
    for i in range(len(robots)):
        robot = robots[i]
        robot = robot.split('=')[1:]
        robot = [r.split(' ')[0].split(',') for r in robot]
        robot = [int(r) for s in robot for r in s]
        robots[i] = tuple(robot)

    def simulateRobot (robot):
        x, y, dx, dy = robot
        return ((x+dx)%m, (y+dy)%n, dx, dy)
    
    def getFrame (robots):
        robotPos = defaultdict(int) 
        interesting = False
        grid = []
        for robot in robots:
            x, y, _, __ = robot
            robotPos[(x,y)] += 1
        for j in range(n):
            row = []
            count = 0 
            for i in range(m):
                if (i,j) in robotPos:
                    row.append(1)
                    count += 1
                else:
                    row.append(0)
                    count = 0
                if count >= 5:
                    # can tweak count to search for contiguous robots present to see interesting patterns
                    interesting = True
            grid.append(row)
        return grid if interesting else None
    
    for i in range(iterations):
        for j in range(len(robots)):
            robots[j] = simulateRobot(robots[j]) 
        frame = getFrame(robots)
        if frame:
            frames.append(frame)
            frameNum.append(i+1)

    fig, ax = plt.subplots()
    im = ax.imshow(frames[0], cmap='gray')
    frame_text = ax.text(3, 0, '', fontsize=12, color='blue')  # Adjust position (3, 0.5) as needed

    def update_plot(i):
        # Add text to display the frame number
        im.set_data(frames[i])
        frame_text.set_text(f'Frame: {frameNum[i]}')
        return im, frame_text 
    
    ani = animation.FuncAnimation(fig=fig, func=update_plot, frames=len(frames), interval=300)
    ani.save('2024/14_easter_egg.webm', writer='ffmpeg', codec='libvpx', bitrate=1000000)
    plt.show()
    # see the animation file for the answer
    return frameNum

def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/14_input.txt", 'r').read()
    example = open("2024/puzzle_input/14_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example, 11, 7)
    p1(input, 101, 103)
    print("\nPart 2:")
    # p2(example)
    p2(input)

if __name__ == "__main__":
    main()
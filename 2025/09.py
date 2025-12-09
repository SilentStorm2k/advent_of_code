import time
import re
from collections import defaultdict, deque
import heapq
import shapely


def execute(func):
    def wrapper(*args):
        t1 = time.time()
        print(f'Answer for {func.__name__} : {func(*args)}')
        t2 = time.time()
        print(f'Executed in : {round(t2-t1, 5)}')
    # if need to reuse p1 w/o decorator use : p1.__original(input)
    wrapper.__original = func
    return wrapper


@execute
def p1(input):
    # just brute force check every pair
    points = [[int(coord) for coord in point.split(',')]
              for point in input.split('\n')]
    maxArea = 0
    for i in range(len(points)):
        for j in range(len(points)):
            if i > j:
                a, b = points[i], points[j]
                curArea = (abs(a[0]-b[0])+1)*(abs(a[1]-b[1])+1)
                maxArea = max(maxArea, curArea)
    return maxArea


@execute
def p2(input):
    # still choosing from the points
    # just that some point pairs might be invalid
    # need to check if all 4 corners will be inside the enclosed
    # tile group
    # tile group is formed by lines connecting adjacent points

    points = [[int(coord) for coord in point.split(',')]
              for point in input.split('\n')]

    polygon = shapely.Polygon(points)

    maxArea = 0
    for i in range(len(points)):
        for j in range(len(points)):
            if i > j:
                x1, y1 = points[i]
                x2, y2 = points[j]

                rect = shapely.box(min(x1, x2), min(y1, y2),
                                   max(x1, x2), max(y1, y2))
                if polygon.contains(rect):
                    curArea = (abs(x1-x2)+1)*(abs(y1-y2)+1)
                    maxArea = max(maxArea, curArea)
    return maxArea


def main():
    # when called from ~/advent_of_code$
    input = open("2025/puzzle_input/09_input.txt", 'r').read()
    example = open("2025/puzzle_input/09_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)


if __name__ == "__main__":
    main()

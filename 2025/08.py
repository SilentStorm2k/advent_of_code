from functools import reduce
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
    # if need to reuse p1 w/o decorator use : p1.__original(input)
    wrapper.__original = func
    return wrapper


@execute
def p1(input, numConnections=1000):
    # lets do my favorite Disjoint union set
    wires = [[int(pos)for pos in wire.split(',')]
             for wire in input.split('\n')]

    sortedWireIdx = sortedWirePairs(wires)
    circuits = DisjointUnionSet(wires)

    for idx in range(numConnections):
        i, j = sortedWireIdx[idx]
        circuits.union(i, j)

    largestCircuits = sorted(circuits.circuits.values(), reverse=True)
    return reduce(lambda x, y: x*y, largestCircuits[:3])


@execute
def p2(input):
    # lets do my favorite Disjoint union set
    wires = [[int(pos)for pos in wire.split(',')]
             for wire in input.split('\n')]

    sortedWireIdx = sortedWirePairs(wires)
    circuits = DisjointUnionSet(wires)

    for i, j in sortedWireIdx:
        circuits.union(i, j)
        if circuits.circuitCount == 1:
            return wires[i][0]*wires[j][0]

    return None


class DisjointUnionSet:
    def __init__(self, wires):
        self.parents = [i for i in range(len(wires))]
        self.circuitCount = len(wires)
        self.circuits = {i: 1 for i in range(len(wires))}

    def findParent(self, idx):
        if self.parents[idx] == idx:
            return idx
        self.parents[idx] = self.parents[self.parents[idx]]
        return self.findParent(self.parents[idx])

    def union(self, i, j):
        # returns True if connection was made, false otherwise
        parentI, parentJ = self.findParent(i), self.findParent(j)
        if parentI == parentJ:
            return False
        elif parentI <= parentJ:
            self.parents[parentJ] = parentI
            self.circuits[parentI] += self.circuits[parentJ]
            del self.circuits[parentJ]
        else:
            self.parents[parentI] = parentJ
            self.circuits[parentJ] += self.circuits[parentI]
            del self.circuits[parentI]
        self.circuitCount -= 1
        return True


def sortedWirePairs(wires):
    # sorted according to distance
    # returns pairs of idx's of the wires closest to each other by dist
    wirePairs = []
    for i in range(len(wires)):
        for j in range(i+1, len(wires)):
            if i == j:
                continue
            wireI, wireJ = wires[i], wires[j]
            dist = (wireI[0]-wireJ[0])**2 + (wireI[1] -
                                             wireJ[1])**2 + (wireI[2]-wireJ[2])**2
            wirePairs.append((dist, i, j))
    return [(wireIdx[1], wireIdx[2]) for wireIdx in sorted(wirePairs)]


def main():
    # when called from ~/advent_of_code$
    input = open("2025/puzzle_input/08_input.txt", 'r').read()
    example = open("2025/puzzle_input/08_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example, 10)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)


if __name__ == "__main__":
    main()

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
    connections = defaultdict(set) 
    # create a dictionary/edge map of the vertices
    for edge in input.split('\n'):
        v1, v2 = edge.split('-')
        connections[v1].add(v2)
        connections[v2].add(v1)
    seen = set()
    def isStronglyConnected (p1, p2, p3, edgeMap):
        # bruteforce checking of strongly connected components
        v1 = p1 in edgeMap[p2] and p1 in edgeMap[p3]
        v2 = p2 in edgeMap[p1] and p2 in edgeMap[p3] 
        v3 = p3 in edgeMap[p1] and p3 in edgeMap[p2]
        return v1 and v2 and v3 

    # Checking for triplet of vertices with k1 starting with t
    for k1,v1 in connections.items():
        if k1[0] != 't':
            continue
        for k2,v2 in connections.items():
            if k2 not in v1 or k1==k2:
                continue
            for k3,v3 in connections.items():
                # if the 3 components are strongly connected, add to seen list
                if isStronglyConnected(k1, k2, k3, connections):
                    lis = sorted([k1,k2,k3])
                    seen.add(tuple(lis))
    return len(seen) 

                    
            

                


    return None
                 
@execute
def p2(input):
    connections = defaultdict(set) 
    maxComponent = set()
    # get the edgemap view of all the vertices and its connected edges
    for edge in input.split('\n'):
        v1, v2 = edge.split('-')
        connections[v1].add(v2)
        connections[v2].add(v1)
    for k1,v in connections.items():
        componentCandidate = deque()
        for k2 in v:
            # the largest connected component with k1, must include some of its neighbors
            componentCandidate.append(set([k1, k2]))
        # building larger and larger components at each iteration
        while componentCandidate:
            l = len(componentCandidate)
            for _ in range(l):
                curConnected = componentCandidate.popleft()
                # update largest seen component so far if applicable
                if len(curConnected) > len(maxComponent):
                    maxComponent = curConnected
                for k3 in v:
                    # adding additional vertex to connected component if its not already 
                    # in the current component (should satisfy being connected to every other vertex)
                    if k3 not in curConnected:
                        connected = True
                        for k in list(curConnected):
                            if k3 not in connections[k]:
                                connected = False
                                break
                        if connected:
                            curConnected.add(k3)
                            componentCandidate.append(curConnected)

    return ','.join(sorted(list(maxComponent))) 
 
def main():
    # when called from ~/advent_of_code$
    input = open("2024/puzzle_input/23_input.txt", 'r').read()
    example = open("2024/puzzle_input/23_example.txt", 'r').read()
    print("\nPart 1:")
    p1(example)
    p1(input)
    print("\nPart 2:")
    p2(example)
    p2(input)

if __name__ == "__main__":
    main()
import time
from collections import deque

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
    input = input.split('\n')
    ends = deque()
    for row in input:
        t, b = row.split('~')
        t = tuple((int(i) for i in t.split(',')))
        b = tuple((int(i) for i in b.split(',')))
        ends.append((t, b))
    
    # sorting blocks by z value
    sorList = sorted(ends, key= lambda e: e[0][2])
    sor = deque()
    for ele in sorList:
        sor.append(ele)
    fallenBlocks = fall(sor)
    safeToDisintegrate = disintegrate(fallenBlocks)
    return len(safeToDisintegrate)

def isCollision(block1, block2):
    b1X = (block1[0][0], block1[1][0])
    b2X = (block2[0][0], block2[1][0])
    b1Y = (block1[0][1], block1[1][1])
    b2Y = (block2[0][1], block2[1][1])
    intersectionX = len(range(max(b1X[0], b2X[0]), min(b1X[1], b2X[1])+1))
    intersectionY = len(range(max(b1Y[0], b2Y[0]), min(b1Y[1], b2Y[1])+1))
    return intersectionX>0 and intersectionY>0

def fall(blocks):
    fallenBlocks = []
    while blocks:
        currentBlock = blocks.popleft()
        x1, y1, x2, y2 = currentBlock[0][0], currentBlock[0][1], currentBlock[1][0], currentBlock[1][1]
        z1, z2 = 1, currentBlock[1][2]-currentBlock[0][2]+1
        if fallenBlocks != []:
            for block in fallenBlocks:
                if isCollision(block, currentBlock):
                    z1, z2 = max(z1, block[1][2]+1), max(z2, currentBlock[1][2] - currentBlock[0][2] + block[1][2]+1)
        fallenBlocks.append(((x1, y1, z1), (x2, y2, z2)))
    return fallenBlocks

def disintegrate(blocks):
    safeToDisintegrate = set()
    sAbove = {b: [] for b in blocks}
    # iterating over blocks, if there is a block immediately above cur
    # and it will overlap if fallen, then cur supports it, add above to list of blocks supported by cur (sAbove)
    for cur in blocks:
        for other in blocks:
            if cur == other:
                continue
            if other[0][2] - cur[1][2] == 1: # other is immediately above cur
                if isCollision(cur, other):
                    sAbove[cur].append(other)
    
    for block in sAbove.keys():
        if sAbove[block] == []:
            safeToDisintegrate.add(block)
        else:
            supportBlocks = sAbove[block]
            count = [0 for _ in range(len(supportBlocks))]
            for otherBlock in sAbove.keys():
                for i, supportBlock in enumerate(supportBlocks):
                    if supportBlock in sAbove[otherBlock]:
                        count[i] += 1
            # if all blocks are supported by at least one other block somewhere, it can be disintegrated
            if all(c >= 2 for c in count):
                safeToDisintegrate.add(block)

    return safeToDisintegrate

@execute
def p2(input):
    return

def main(args=None):
    # when called from ~/Code/repos/advent_of_code$
    example = open("2023/day 22/puzzle_input/example.txt", 'r').read()
    input = open("2023/day 22/puzzle_input/input.txt", 'r').read()
    print(f'\nPart 1:')
    p1(example)
    p1(input)
    # EXPECTED ANSWER 463
    # print(f'\nPart 2:')
    # p2(example)
    # p2(input)


if __name__ == '__main__':
    main()

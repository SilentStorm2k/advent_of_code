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
        flag = False
        x1, y1, x2, y2 = currentBlock[0][0], currentBlock[0][1], currentBlock[1][0], currentBlock[1][1]
        if fallenBlocks != []:
            # for block in list(sorted(fallenBlocks, key= lambda e: e[0][2], reverse=True)):
            for block in list(reversed(fallenBlocks)):
                if isCollision(block, currentBlock):
                    z1, z2 = block[1][2]+1, currentBlock[1][2] - currentBlock[0][2] + block[1][2]+1
                    fallenBlocks.append(((x1, y1, z1), (x2, y2, z2)))
                    flag = True
                    break
        if not flag:
            fallenBlocks.append(((x1, y1, 1), (x2, y2, currentBlock[1][2]-currentBlock[0][2]+1)))
    return fallenBlocks

def disintegrate(blocks):
    safeToDisintegrate = set()
    # for b in blocks:
    #     prior = list(blocks)
    #     prior.remove(b)
    #     # prior = sorted(prior2, key= lambda e: e[0][2])
    #     temp = deque()
    #     for c in prior:
    #         temp.append(c)
    #     simulate = fall(temp)
    #     if simulate == prior:
    #         safeToDisintegrate.add(b)

    # return safeToDisintegrate
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
    
    a1, a2 = 0, 0 
    for block in sAbove.keys():
        if sAbove[block] == []:
            a1 += 1
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
                a2 += 1
    print(a1, a2)
    return safeToDisintegrate

# @execute
# def p1(input):
#     input = input.split('\n')
#     ends = []
#     for row in input:
#         t, b = row.split('~')
#         t = tuple([int(i) for i in t.split(',')])
#         b = tuple([int(i) for i in b.split(',')])
#         ends.append((t, b))
    
#     # assuming that cubes extend towards the axises
#     sor = sorted(ends, key= lambda e: e[0][2])
#     fallenBlocks = []
#     flag = False

#     # simulate falling
#     for i in range(len(sor)):
#         current = sor[i]
#         flag = False
#         for j in range(len(fallenBlocks)-1, -1, -1):
#             below = fallenBlocks[j]
#             if flag: break
#             if isCollision(current, below):
#                 botZ = below[1][2]+1
#                 new = ((current[0][0], current[0][1], botZ), (current[1][0], current[1][1], current[1][2]-current[0][2]+botZ))
#                 fallenBlocks.append(new)
#                 flag = True
#         if not flag: 
#             new = ((current[0][0], current[0][1], 1), (current[1][0], current[1][1], current[1][2]-current[0][2]+1))
#             fallenBlocks.append(new)

#     sAbove = {i:[] for i in range(len(fallenBlocks))}
#     # sAbove = {}
#     # iterating over blocks, if there is a block immediately above cur
#     # and it will overlap if fallen, then cur supports it, add above to list of blocks supported by cur (sAbove)
#     for i in range(len(fallenBlocks)):
#         cur = fallenBlocks[i]
#         # ab = []
#         for j in range(i+1, len(fallenBlocks)):
#             above = fallenBlocks[j]
#             if above[0][2] - cur[1][2] != 1:
#                 continue
#             if isCollision(cur, above):
#                 sAbove[i].append(j)
#                 # ab.append(j)
#         # sAbove.update({i : ab})


#     # print(fallenBlocks)
#     # print(sAbove)
#     ans = 0
#     ans1 = 0
#     ans2 = 0
#     for b in range(len(fallenBlocks)):
#         # not supporting any blocks, hence can be disintegrated
#         if sAbove.get(b) == []:
#             ans += 1
#             ans1 += 1
#         else:
#             vals = sAbove.get(b)
#             count = [0 for _ in range(len(vals))]
#             for k in sAbove.keys():
#                 for i, val in enumerate(vals):
#                     if val in sAbove.get(k):
#                         count[i] += 1
#             # if all blocks are supported by at least one other block somewhere, it can be disintegrated
#             if all(c >= 2 for c in count):
#                 ans += 1
#                 ans2 += 1
    
#     print(get_safe_bricks(sAbove, fallenBlocks))
#     print(len(sAbove))
#     print(len(fallenBlocks))

#     # print(ans1)
#     # print(ans2)
#     # print(fallenBlocks)
#     # print(sAbove)
#     return ans

# def isCollision(block1, block2):
#     b1X = (block1[0][0], block1[1][0])
#     b2X = (block2[0][0], block2[1][0])
#     b1Y = (block1[0][1], block1[1][1])
#     b2Y = (block2[0][1], block2[1][1])
#     intersectionX = max(b1X[0], b2X[0]) == min(b1X[1], b2X[1]) or min(b1X[0], b2X[0]) == max(b1X[1], b2X[1])
#     intersectionY = max(b1Y[0], b2Y[0]) == min(b1Y[1], b2Y[1]) or min(b1Y[0], b2Y[0]) == max(b1Y[1], b2Y[1])
#     return intersectionX and intersectionY

# def get_safe_bricks(support_stats, fallenBlocks):
#     can_be_disintegrated = 0
#     for brick_id, supporting_bricks in support_stats.items():
#        other_values = set([s for brick, supports in support_stats.items() for s in supports  if brick != brick_id])
#        if len(supporting_bricks) - len(other_values.intersection(set(supporting_bricks))) == 0:
#            can_be_disintegrated += 1
    
#     return can_be_disintegrated + len(fallenBlocks) - len(support_stats)

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

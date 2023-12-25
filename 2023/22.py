import time

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
    ends = []
    for row in input:
        t, b = row.split('~')
        t = tuple([int(i) for i in t.split(',')])
        b = tuple([int(i) for i in b.split(',')])
        ends.append((t, b))
    
    # assuming that cubes extend towards the axises
    sor = sorted(ends, key= lambda e: e[0][2])
    fallenBlocks = []
    flag = False

    # simulate falling
    for i in range(len(sor)):
        current = sor[i]
        flag = False
        for j in range(len(fallenBlocks)-1, -1, -1):
            below = fallenBlocks[j]
            if flag: break
            if isCollision(current, below):
                botZ = below[1][2]+1
                new = ((current[0][0], current[0][1], botZ), (current[1][0], current[1][1], current[1][2]-current[0][2]+botZ))
                fallenBlocks.append(new)
                flag = True
        if not flag: 
            new = ((current[0][0], current[0][1], 1), (current[1][0], current[1][1], current[1][2]-current[0][2]+1))
            fallenBlocks.append(new)

    sAbove = {i:[] for i in range(len(fallenBlocks))}
    # sAbove = {}
    # iterating over blocks, if there is a block immediately above cur
    # and it will overlap if fallen, then cur supports it, add above to list of blocks supported by cur (sAbove)
    for i in range(len(fallenBlocks)):
        cur = fallenBlocks[i]
        # ab = []
        for j in range(i+1, len(fallenBlocks)):
            above = fallenBlocks[j]
            if above[0][2] - cur[1][2] != 1:
                continue
            if isCollision(cur, above):
                sAbove[i].append(j)
                # ab.append(j)
        # sAbove.update({i : ab})


    # print(fallenBlocks)
    # print(sAbove)
    ans = 0
    ans1 = 0
    ans2 = 0
    for b in range(len(fallenBlocks)):
        # not supporting any blocks, hence can be disintegrated
        if sAbove.get(b) == []:
            ans += 1
            ans1 += 1
        else:
            vals = sAbove.get(b)
            count = [0 for _ in range(len(vals))]
            for k in sAbove.keys():
                for i, val in enumerate(vals):
                    if val in sAbove.get(k):
                        count[i] += 1
            # if all blocks are supported by at least one other block somewhere, it can be disintegrated
            if all(c >= 2 for c in count):
                ans += 1
                ans2 += 1
    
    print(get_safe_bricks(sAbove, fallenBlocks))
    print(len(sAbove))
    print(len(fallenBlocks))

    # print(ans1)
    # print(ans2)
    # print(fallenBlocks)
    # print(sAbove)
    return ans

def isCollision(block1, block2):
    b1X = (block1[0][0], block1[1][0])
    b2X = (block2[0][0], block2[1][0])
    b1Y = (block1[0][1], block1[1][1])
    b2Y = (block2[0][1], block2[1][1])
    intersectionX = max(b1X[0], b2X[0]) == min(b1X[1], b2X[1]) or min(b1X[0], b2X[0]) == max(b1X[1], b2X[1])
    intersectionY = max(b1Y[0], b2Y[0]) == min(b1Y[1], b2Y[1]) or min(b1Y[0], b2Y[0]) == max(b1Y[1], b2Y[1])
    return intersectionX and intersectionY

def get_safe_bricks(support_stats, fallenBlocks):
    can_be_disintegrated = 0
    for brick_id, supporting_bricks in support_stats.items():
       other_values = set([s for brick, supports in support_stats.items() for s in supports  if brick != brick_id])
       if len(supporting_bricks) - len(other_values.intersection(set(supporting_bricks))) == 0:
           can_be_disintegrated += 1
    
    return can_be_disintegrated + len(fallenBlocks) - len(support_stats)

@execute
def p2(input):
    return

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 22/puzzle_input/example3.txt" if ex else "2023/day 22/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
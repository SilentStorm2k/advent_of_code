import sys
import re
import time

class Function:
    def __init__(self, S):
        lines = S.split('\n')[1:]
        self.tuples: list[tuple[int, int, int]] = [[int(x) for x in line.split()] for line in lines]
    
    def f1(self, x: int) -> int:
        for (dst, src, sz) in self.tuples:
            if src<=x<src+sz:
                return dst+x-src
        return x
    
    def f2(self, R):
        A = []
        for (dst, src, sz) in self.tuples:
            src_end = src + sz
            NR = []
            while R:
                (st, ed) = R.pop()
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0]:
                    NR.append(before)
                if inter[1]>inter[0]:
                    A.append((inter[0]-src+dst, inter[1]-src+dst))
                if after[1] > after[0]:
                    NR.append(after)
            R = NR        
        return A+R
    
def func(input_data):
    parts = input_data.split('\n\n')
    seeds, *others = parts
    seed = [int(x) for x in re.split(r':', seeds)[1].split()]
    Fs = [Function(s) for s in others]
    P1 = []
    for x in seed:
        val = x
        for f in Fs:
            val = f.f1(val)
        P1.append(val)
    
    P2 = []
    pairs = list(zip(seed[::2], seed[1::2]))
    for st, sz in pairs:
        R = [(st, st+sz)]
        # print(f'Seeds: {R}')
        for f in Fs:
            R = f.f2(R)
            # print(R)
        P2.append(min(R)[0])

    return min(P1), min(P2)







# when called from ~/Code/repos/advent_of_code$
ex_file = open("2023/day 5/puzzle_input/day_5.txt", 'r')
# ex_file = open("2023/day 5/puzzle_input/day_5_p1_example.txt", 'r')
input = ex_file.read()
# print(text)
t0 = time.time()
print(f"Answer is : {func(input)}")
t1 = time.time()
print(f"Executed in {round(t1-t0, 5)}s")
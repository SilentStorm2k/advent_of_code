import os
import time

def func(input):
    time, dist = input.split('\n')
    time, dist = [int(t) for t in time.split(':')[1].split()], [int(t) for t in dist.split(':')[1].split()]
    
    ways = []
    for no, t in enumerate(time):
        cs = t
        c_ways = 0
        for i in range(0, t//2+1):
            cur_dist = cs*i
            
            if cur_dist > dist[no]:
                c_ways = c_ways + (1 if (i == t//2 and t%2==0) else 2)
            cs -= 1
        ways.append(c_ways)

    ret = 1
    for way in ways:
        ret *= way
    return ret

# when called from ~/Code/repos/advent_of_code$
ex_file = open("2023/day 6/puzzle_input/day_6.txt", 'r')
# ex_file = open("2023/day 6/puzzle_input/day_6_example.txt", 'r')
input = ex_file.read()
# print(text)
t0 = time.time()
print(f"Answer is : {func(input)}")
t1 = time.time()
print(f"Executed in {round(t1-t0, 5)}s")
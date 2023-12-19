import os
import time

def func(input):
    time, dist = input.split('\n')
    time, dist = int("".join(time.split(':')[1].split())), int("".join(dist.split(':')[1].split()))
    print(f'{time}, {dist}')
    
    
    c_ways = 0
    cs = time
    isEven = time%2==0
    mid = time//2
    for i in range(0, mid+1):
        cur_dist = cs*i
            
        if cur_dist > dist:
            c_ways = c_ways + (1 if (i == mid and isEven) else 2)
        cs -= 1
    
    return c_ways

# when called from ~/Code/repos/advent_of_code$
ex_file = open("2023/day 6/puzzle_input/day_6.txt", 'r')
# ex_file = open("2023/day 6/puzzle_input/day_6_example.txt", 'r')
input = ex_file.read()
# print(text)
t0 = time.time()
print(f"Answer is : {func(input)}")
t1 = time.time()
print(f"Executed in {round(t1-t0, 5)}s")
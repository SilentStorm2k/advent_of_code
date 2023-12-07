import os
import time

def func(input):
    return 

# when called from ~/Code/repos/advent_of_code$
ex_file = open("2023/day 7/puzzle_input/day_7.txt", 'r')
# ex_file = open("2023/day 7/puzzle_input/day_7_example.txt", 'r')
input = ex_file.read()
# print(text)
t0 = time.time()
print(f"Answer is : {func(input)}")
t1 = time.time()
print(f"Executed in {round(t1-t0, 5)}s")
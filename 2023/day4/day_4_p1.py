import os
import re

def func(input):
    input = input.split('\n')
    # print(input)
    total_points = 0
    for card in input:
        current_points = 0
        c = re.split(r'[\:\|]', card)
        # print(c)
        winners = c[1].split()
        yours = c[2].split()
        for nums in yours:
            if nums in winners:
                if current_points == 0:
                    current_points = current_points + 1
                else:
                    current_points = current_points*2
        total_points = total_points + current_points
    return total_points

# when called from ~/Code/repos/advent_of_code$
ex_file = open("2023/day4/puzzle_input/day_4.txt", 'r')
# ex_file = open("2023/day4/puzzle_input/day_4_p1_example.txt", 'r')
input = ex_file.read()
# print(input)
print(f"Answer is : {func(input)}")
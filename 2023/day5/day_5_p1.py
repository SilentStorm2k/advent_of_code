import os
import re
import time

def func(input):
    split_input = re.split(r'(\n\n)', input)
    split_input = [j for i,j in enumerate(split_input) if j!="\n\n"]
    seeds = re.split(r'[:]', split_input[0])[1].split()
    seed_soils = re.split(r'[:]', split_input[1])[1].split('\n')[1:]
    so_fert = re.split(r'[:]', split_input[2])[1].split('\n')[1:]
    fert_wat = re.split(r'[:]', split_input[3])[1].split('\n')[1:]
    wat_lit = re.split(r'[:]', split_input[4])[1].split('\n')[1:]
    lit_temp = re.split(r'[:]', split_input[5])[1].split('\n')[1:]
    temp_humd = re.split(r'[:]', split_input[6])[1].split('\n')[1:]
    humd_loc = re.split(r'[:]', split_input[7])[1].split('\n')[1:]
    
    seed_loc = []
    for s in seeds:
        s = int(s)
        soil = loc(s, seed_soils)
        fert = loc(soil, so_fert)
        water = loc(fert, fert_wat)
        light = loc(water, wat_lit)
        temp = loc(light, lit_temp)
        humd = loc(temp, temp_humd)
        location = loc(humd, humd_loc)
        seed_loc.append(location)
    
    # print(seeds)
    # print(seed_soils)
    # print(so_fert)
    # print(fert_wat)
    # print(wat_lit)
    # print(lit_temp)
    # print(temp_humd)
    # print(humd_loc)
    # print(seed_loc)
    return min(seed_loc)

def loc(val, list_of_loc):
    val = int(val)
    ret = val
    for lis in list_of_loc:
        lis = lis.split()
        src, dest, rang = int(lis[0]), int(lis[1]), int(lis[2])
        if val in range(dest, dest + rang):
            ret = (val - dest) + src
            return ret
    return ret
        
# when called from ~/Code/repos/advent_of_code$
ex_file = open("2023/day5/puzzle_input/day_5.txt", 'r')
# ex_file = open("2023/day5/puzzle_input/day_5_p1_example.txt", 'r')
input = ex_file.read()
# print(text)
t0 = time.time()
print(f"Answer is : {func(input)}")
t1 = time.time()
print(f"Executed in {round(t1-t0, 5)}s")
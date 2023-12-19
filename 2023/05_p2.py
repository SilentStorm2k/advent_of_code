import os
import re
import sys
import time
import numpy as np

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
    
    ssr, sfr, fwr, wlr, ltr, thr, hlr = r(seed_soils), r(so_fert), r(fert_wat), r(wat_lit), r(lit_temp), r(temp_humd), r(humd_loc)
    s1, s2, s3, s4, s5, s6, s7 = list(ssr.keys()), list(sfr.keys()), list(fwr.keys()), list(wlr.keys()), list(ltr.keys()), list(thr.keys()), list(hlr.keys())
    ss1, ss2, ss3, ss4, ss5, ss6, ss7 = sorted(s1), sorted(s2), sorted(s3),sorted(s4), sorted(s5), sorted(s6), sorted(s7)
    ssr_, sfr_, fwr_, wlr_, ltr_, thr_, hlr_ = {i: ssr[i] for i in ss1}, {i: sfr[i] for i in ss2}, {i: fwr[i] for i in ss3}, {i: wlr[i] for i in ss4}, {i: ltr[i] for i in ss5}, {i: thr[i] for i in ss6}, {i: hlr[i] for i in ss7}

    seed_range = []
    for i, s in enumerate(seeds):
        if i%2 != 0:
            # print(f"{i}, {int((i+1)/2) - 1}, {s}, {seeds[i-1]}")
            seed_range.append((int(seeds[i-1]), int(seeds[i-1]) + int(s)))
    seed_range.sort()

    size = 0
    # t1 = time.time()
    # for r in seed_range:
    #     for s in range(int(r[0]), int(r[1])):
    #         size = size + 1
    # t2 = time.time()
    # print(f'size = {size}, time taken = {round(t2-t1, 5)}')
    min = sys.maxsize
    i = 0
    t1 = time.time()
    for s in seed_range:
        for seed in range(s[0], s[1]):
            if i%1000000 == 0:
                t2 = time.time()
                print(f'i: {i}, time: {round(t2-t1, 5)}')
                t1 = time.time()
            i = i + 1
            # seed = int(seed)
            # soil = loc(seed, seed_soils)
            # fert = loc(soil, so_fert)
            # water = loc(fert, fert_wat)
            # light = loc(water, wat_lit)
            # temp = loc(light, lit_temp)
            # humd = loc(temp, temp_humd)
            # location = loc(humd, humd_loc)

            seed = int(seed)
            soil = dic_loc(seed, ssr_)
            fert = dic_loc(soil, sfr_)
            water = dic_loc(fert, fwr_)
            light = dic_loc(water, wlr_)
            temp = dic_loc(light, ltr_)
            humd = dic_loc(temp, thr_)
            location = dic_loc(humd, hlr_)
            # print(f'{seed}, {soil}, {fert}, {water}, {light}, {temp}, {humd}, {location}')
            if min > location:
                min = location
    print(i)
    return min


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

def dic_loc(val, dic):
    ret = int(val)
    left, right = 0, len(dic) - 1
    
    keys = list(dic)
    values = list(dic.values())
    # print(keys)
    # print(values)

    while left <= right:
        mid = (left + right) // 2
        if keys[mid][0] <= val < keys[mid][1]:
            ret = (val - keys[mid][0]) + values[mid][0] 
            return ret
        elif keys[mid][0] > val:
            right = mid - 1
        else:
            left = mid + 1
    return ret
    
def r(lis):
    ret = {}
    for l in lis:
        l = l.split()
        ret.update({(int(l[1]), int(l[1]) + int(l[2])) : (int(l[0]), int(l[0]) + int(l[2]))})
    # print(ret)
    return ret
# def rev_loc(loc, list_of_p.sort()re):
#     loc = int(loc)
#     # if (loc == sys.maxsize):
#     #     return loc
#     ret = loc
#     for lis in list_of_p.sort()re:
#         lis = lis.split()
#         src, dest, rang = int(lis[0]), int(lis[1]), int(lis[2])
#         if loc in range(src, src + rang):
#             ret = (loc - src) + dest
#             return ret
#     return ret

# def is_valid_seed(seed, seed_range):
#     for i, s in enumerate(seed_range):
#         if seed in range(s[0], s[0]+s[1]):
#             return True, i
#     return False, -1


# when called from ~/Code/repos/advent_of_code$
ex_file = open("2023/day 5/puzzle_input/day_5.txt", 'r')
# ex_file = open("2023/day 5/puzzle_input/day_5_p1_example.txt", 'r')
input = ex_file.read()
# print(text)
t0 = time.time()
print(f"Answer is : {func(input)}")
t1 = time.time()
print(f"Executed in {round(t1-t0, 5)}s")
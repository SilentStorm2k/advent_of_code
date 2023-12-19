import time
import re

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
    seq = input.split(',')
    sum = 0
    for cha in seq:
        sum += hashVal(cha, p1=True)
    return sum

@execute
def p2(input):
    seq = input.split(',')
    boxes = dict()
    for cha in seq:
        box_num = hashVal(cha, p1=False)
        key = re.split(r'[-=]', cha)[0]
        lens_val = re.search(r'[0-9]', cha)
        lens_val = int(lens_val.group()) if lens_val else None
        if lens_val:
            val = {} if not boxes.get(box_num) else boxes.get(box_num) 
            val.update({key: lens_val})
            boxes.update({box_num:val})
        else:
            val = boxes.get(box_num)
            if val and key in val.keys(): 
                del val[key]
            boxes.update({box_num:val})

    focusing_power = 0
    for l in boxes.keys():
        slotNum = 1
        lenses = boxes.get(l)
        for lens in lenses.keys():
            focusing_power += (l+1) * slotNum * lenses.get(lens)
            slotNum += 1

    return focusing_power

def hashVal(seq, p1):
    val = 0
    for s in list(seq):
        if not p1:
            if s == '=' or s == '-':
                break
        val += ord(s)
        val *= 17
        val %= 256
    return val


# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 15/puzzle_input/example.txt" if ex else "2023/day 15/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
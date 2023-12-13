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
def p1(input, part2 = 0):
    pattern = input.split('\n\n')
    sum = 0
    for p in pattern:
        rows = p.split('\n')
        cols = ['' for r in rows[0]]
        for i, r in enumerate(rows):
            for j, c in enumerate(list(r)):
                cols[j] += c
        rowmirr, colmirr =  getMirror(rows, part2), getMirror(cols, part2)
        sum += colmirr + 100*rowmirr

    return sum

@execute
def p2(input):
    return p1.__original(input, 1)

# returns true if string values are off by one or same 
def isSmudge(string1, string2):
    count_diffs = 0
    for a, b in zip(string1, string2):
        if a!=b:
            if count_diffs: return False
            count_diffs += 1
    return True

# returns index value of mirror location
def getMirror(cols, part2):
    for i in range(1, len(cols)):
            smudge = 0
            if isSmudge(cols[i], cols[i-1]):
                if cols[i] != cols[i-1]:  
                    smudge += 1 
                mini = min(i, len(cols)-i)
                count = 0
                for j in range(i+1, i + mini):  
                    if isSmudge(cols[j], cols[i-(j-i)-1]):
                        if cols[j] != cols[i-(j-i)-1]:
                            smudge += 1
                        count += 1
                if count == len(range(i+1, i + mini)) and (smudge == 1 if part2 else smudge == 0):
                    return i
    return 0
# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 13/puzzle_input/example.txt" if ex else "2023/day 13/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
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
    pattern = input.split('\n\n')
    sum = 0
    olor = []
    for p in pattern:
        rows = p.split('\n')
        cols = ['' for r in rows[0]]

        for i, r in enumerate(rows):
            for j, c in enumerate(list(r)):
                cols[j] += c

        rowmirr, colmirr = 0,0
        for i in range(1, len(cols)):
            if cols[i] == cols[i-1]:
                mini = min(i, len(cols)-i-1)
                leftcol, rightcol = [], []
                for j in range(i-1, i-1 - mini, -1):
                    leftcol.append(cols[j])
                for j in range(i, i + mini):  
                    rightcol.append(cols[j])
                if rightcol==leftcol:
                    colmirr = i
                    break
        for i in range(1, len(rows)):
            if rows[i] == rows[i-1]:
                mini = min(i, len(rows)-i)
                leftcol, rightcol = [], []
                for j in range(i-1, i-1 - mini, -1):
                    leftcol.append(rows[j])
                for j in range(i, i + mini):  
                    rightcol.append(rows[j])
                if rightcol==leftcol:
                    rowmirr = i
                    break
        # print(f'{rowmirr}, {colmirr}')
        
        sum += colmirr + 100*rowmirr
        
    return sum

@execute
def p2(input):
    # s, olor = p1.__original(input) 
    pattern = input.split('\n\n')
    sum = 0
    for n, p in enumerate(pattern):
        rows = p.split('\n')
        cols = ['' for r in rows[0]]

        for i, r in enumerate(rows):
            for j, c in enumerate(list(r)):
                cols[j] += c

        rowmirr, colmirr = 0,0

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

                if count == len(range(i+1, i + mini)) and smudge == 1:
                    colmirr = i
                    break
        
        for i in range(1, len(rows)):
            smudge = 0
            if isSmudge(rows[i], rows[i-1]):
                if rows[i] != rows[i-1]:  
                    smudge += 1 
                mini = min(i, len(rows)-i)
                count = 0
                for j in range(i+1, i + mini):  
                    if isSmudge(rows[j], rows[i-(j-i)-1]):
                        if rows[j] != rows[i-(j-i)-1]:
                            smudge += 1
                        count += 1

                if count == len(range(i+1, i + mini)) and smudge == 1:
                    rowmirr = i
                    break
        sum += colmirr + 100*rowmirr
        # n = 12, 20, 24, 29, 33, 36, 40, 41
    return sum
def isSmudge(string1, string2):
    count_diffs = 0
    for a, b in zip(string1, string2):
        if a!=b:
            if count_diffs: return False
            count_diffs += 1
    return True

# when called from ~/Code/repos/advent_of_code$
ex = 1
input = open("2023/day 13/puzzle_input/example.txt" if ex else "2023/day 13/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)


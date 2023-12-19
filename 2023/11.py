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
def p1(input, expansion_rate = 2):
    # get rows and columns
    rows = input.split('\n')
    cols = ['' for r in rows]
    for i, r in enumerate(rows):
        for j, c in enumerate(list(r)):
            cols[j] += c
    rows_to_expand = []
    cols_to_expand = []

    # finding rows where stars dont exist (for expansion purposes)
    for i, r in enumerate(rows):
        no_star = True 
        for s in list(r):
            if s == '#':
                no_star = False
        if no_star:
            rows_to_expand.append(i)
    
    # likewise finding cols where stars dont exist (for expansion purposes)
    for j, c in enumerate(cols):
        no_star = True 
        for s in list(c):
            if s == '#':
                no_star = False
        if no_star:
            cols_to_expand.append(j)

    # getting coordinates of each star (accommodating for space expansion)
    star_coords = set()
    for i, r in enumerate(rows):
        for j, c in enumerate(list(r)):
            if c == '#':
                x = i
                y = j
                for row in rows_to_expand:
                    if i>row:
                        # counting number of empty rows to increment star's x coordinate by
                        x += expansion_rate-1
                for col in cols_to_expand:
                    if j>col:
                        # counting number of empty cols to increment star's y coordinate by
                        y += expansion_rate-1
                star_coords.add((x, y))
    # sorting to iterate through set
    star_coords = sorted(star_coords)
    dists = 0
    # finding distance (manhattan as told by prompt) between every star and adding them
    for i, star in enumerate(star_coords):
        for j in range(i, len(star_coords)):
            dists += abs(star[0]-star_coords[j][0]) + abs(star[1]-star_coords[j][1])
    return dists

@execute
def p2(input):
    # increasing expansion rate to 1000000 as said by prompt
    return p1.__original(input, 1000000)

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 11/puzzle_input/example.txt" if ex else "2023/day 11/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
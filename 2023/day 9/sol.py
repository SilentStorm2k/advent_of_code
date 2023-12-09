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
def p1(input, part1):
    input = input.split('\n')
    sequences = []
    seq = [s for s in input]
    [sequences.append([int(k) for k in s.split()]) for s in seq]
    # reverse all sequences if part1 (to predict the last digit (first w reversed))
    if part1: sequences = [s[::-1] for s in sequences]
    sum = 0
    for s in sequences:
        sum += s[0] + (1 if part1 else -1)* predict(s, part1) 
    return sum

@execute
def p2(input):
    return p1.__original(input, 0)

def predict(sequence, part):
    # if sequence too short return (as cannot extrapolate anything)
    if len(sequence) == 0 or len(sequence) == 1:
        return None
    # only return when at least 2 members of sequence are 0 (as a double checking)
    if len(sequence) == 2 and sequence[0] == 0 and sequence[1] == 0:
        return 0
    # if not a terminating sequence return ([0,0] is only terminating seq)
    if len(sequence) == 2:
        return None
    # got to start just with last element, and increment
    for i in range(0, len(sequence)):
        # building new sequence of differences from sequence ( below is accounting for whether seq is reversed or not)
        new_list = [sequence[j+1]-sequence[j] for j in range(0, i)] if not part else [sequence[j]-sequence[j+1] for j in range(0, i)]
        k = predict(new_list, part)
        # if empty sequence or sequence too short to extrapolate, increase new  seq len and try again
        # however, when terminating sequence reached (we have enough data to predict next/pre element)
        if k != None:
            # adding or subtracting based on predicting next or previous element
            return new_list[0] + (1 if part else -1)*k 

    # when nothing could be extrapolated from the current sequence (return None, and continue exploring recursively)
    return None


# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 9/puzzle_input/example.txt" if ex else "2023/day 9/puzzle_input/input.txt", 'r').read()
p1(input, True)
p2(input)
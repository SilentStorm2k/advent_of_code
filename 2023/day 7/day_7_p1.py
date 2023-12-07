import time
import string_utils
import itertools
from functools import cmp_to_key

def execute(func):
    def wrapper(*args):   
        t1 = time.time()
        print(f'Answer is : {func(*args)}')
        t2 = time.time()
        print(f'Executed in : {round(t2-t1, 5)}')
    return wrapper

@execute
def func(input):
    input = input.split('\n')
    # corresponding bid for hand
    hand_bid = {s.split()[0]: int(s.split()[1]) for s in input}
    
    type = {}
    # assigning each hand its type value (5 of a kind -> 7, ... high card -> 1)
    for hand in hand_bid.keys():
        type.update({hand: get_type(hand)})
    
    # splitting hand values according to its type (for sorting later)
    s = {i: {k: type[k] for k in type if type[k] == i} for i in range(1, 8)}

    # sorting each hand value in each type according to card values 
    s_sorted = [sorted(s[i], key=cmp_to_key(comp)) for i in range(1, 8)]

    # combining all hands for iteration
    s_rank = list(itertools.chain.from_iterable(s_sorted))
    
    winnings = 0
    # calculating winnings for each hand (its rank  x its  bid)
    for i, hand in enumerate(s_rank):
        # i is rank here since they are sorted
        winnings += (i+1)*hand_bid[hand]

    return winnings

card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7,
               '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
def comp(hand1, hand2):
    for i in range(0, len(hand1)):
        val = card_values[hand1[i]] - card_values[hand2[i]]
        if val != 0:
            return val
    return 0
def get_type(hand):
    ch = []
    for c in hand:
        ch.append(c)
    ch_set = set(ch)  
    if len(ch_set) == 1:
        return 7                # 5 of a kind
    if len(ch_set) == 2:
        count = 0
        for c in ch:
            if c == ch[0]:
                count += 1
        if count == 1 or count == 4:
            return 6            # 4 of a kind
        return 5                # full house
    if len(ch_set) == 3:
        count = 0
        for c in ch:
            if c == ch[0]:
                count += 1
        if count == 1:
            # hack to not write extra code (rerun until starting character is a repeat)
            return get_type(string_utils.shuffle(hand))
        if count == 2:  # count=2 more likely to happen than count=3
            return 3            # 2 pair
        return 4                # 3 of a kind
    if len(ch_set) == 4:
        return 2                # 1 pair
    return 1                    # high card
     

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 7/puzzle_input/day_7_example.txt" if ex else "2023/day 7/puzzle_input/day_7.txt", 'r').read()
func(input)
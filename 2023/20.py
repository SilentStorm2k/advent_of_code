import time
from collections import deque
from math import lcm

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
    input = input.split('\n')
    modType = {}
    modDest = {}
    for line in input:
        mod, dest = line.strip().split('->')
        name, t = mod[1:].strip(), mod[0]
        if t == 'b':
            name, t = mod.strip(), mod.strip()
        dest = [i.strip() for i in dest.split(',')]
        modType.update({name: t})
        modDest.update({name: dest})
    ffState = {mod: 0 for mod in modType.keys() if modType.get(mod) == '%'}
    conjPre = {mod: {} for mod in modType.keys() if modType.get(mod) == '&'}
    for mod in modDest.keys():
        for dest in modDest.get(mod):
            if dest in conjPre.keys():
                conjPre[dest][mod] = 0
    hiP, lowP = 0, 0
    buttonPresses = 1000
    while buttonPresses > 0:
        pulses = deque()
        pulses.append((0, 'broadcaster', 'broadcaster'))
        while pulses:
            pulseVal, mod, sender = pulses.popleft()
            # print(f'{sender} -{"high" if pulseVal else "low"}-> {mod}')
            hiP += 1 if pulseVal else 0
            lowP += 1 if not pulseVal else 0
            if mod not in modType.keys():
                continue
            if mod == 'broadcaster':
                for dest in modDest[mod]:
                    pulses.append((pulseVal, dest, mod))
            if modType[mod] == '%':
                if pulseVal == 0:
                    retP = 0 if ffState[mod] else 1
                    ffState.update({mod: retP})
                    for dest in modDest[mod]:
                        pulses.append((retP, dest, mod))
            if modType[mod] == '&':
                conjPre[mod][sender] = pulseVal
                retP = 1
                if all(conjPre[mod].values()):
                    retP = 0
                for dest in modDest[mod]:
                    pulses.append((retP, dest, mod))
        buttonPresses -= 1

    # print(f'\nHigh = {hiP}, low = {lowP}')
    return hiP * lowP

@execute
def p2(input):
    input = input.split('\n')
    modType = {}
    modDest = {}
    for line in input:
        mod, dest = line.strip().split('->')
        name, t = mod[1:].strip(), mod[0]
        if t == 'b':
            name, t = mod.strip(), mod.strip()
        dest = [i.strip() for i in dest.split(',')]
        modType.update({name: t})
        modDest.update({name: dest})
    ffState = {mod: 0 for mod in modType.keys() if modType.get(mod) == '%'}
    conjPre = {mod: {} for mod in modType.keys() if modType.get(mod) == '&'}
    timeToConj = {mod: {} for mod in modType.keys() if modType.get(mod) == '&'}
    for mod in modDest.keys():
        for dest in modDest.get(mod):
            if dest in conjPre.keys():
                conjPre[dest][mod] = 0
                timeToConj[dest][mod] = 0 

    # using 2 assumptions
    # 1: only 1 mod connects to 'rx' and its a conjunction (calling it finalModDad)
    # 2: mods connecting to finalModDad are also conjunctions
                
    finalMod = 'rx'
    finalVals = {}
    for mod in modType.keys():
        if finalMod in modDest[mod]:
            finalModDad = mod       
    for mod in modType.keys():
        if finalModDad in modDest[mod]:
            finalVals[mod] = 0

    hiP, lowP = 0, 0
    buttonPresses = 1    
    while lcm(*finalVals.values()) == 0:
        pulses = deque()
        pulses.append((0, 'broadcaster', 'broadcaster'))
        while pulses:
            pulseVal, mod, sender = pulses.popleft()
            if mod in finalVals.keys() and pulseVal == 0:
                finalVals[mod] = buttonPresses

            # print(f'{sender} -{"high" if pulseVal else "low"}-> {mod}')
            hiP += 1 if pulseVal else 0
            lowP += 1 if not pulseVal else 0
            if mod not in modType.keys():
                continue
            if mod == 'broadcaster':
                for dest in modDest[mod]:
                    pulses.append((pulseVal, dest, mod))
            if modType[mod] == '%':
                if pulseVal == 0:
                    retP = 0 if ffState[mod] else 1
                    ffState.update({mod: retP})
                    for dest in modDest[mod]:
                        pulses.append((retP, dest, mod))
            if modType[mod] == '&':
                conjPre[mod][sender] = pulseVal
                retP = 1
                if all(conjPre[mod].values()):  
                    retP = 0
                for dest in modDest[mod]:
                    pulses.append((retP, dest, mod))
        buttonPresses += 1

    return lcm(*finalVals.values())



def main():
    # when called from ~/Code/repos/advent_of_code$
    example = open("2023/day 20/puzzle_input/example.txt", 'r').read()
    input = open("2023/day 20/puzzle_input/input.txt", 'r').read()
    print(f'\nPart 1:')
    p1(example)
    p1(input)
    print(f'\nPart 2:')
    # p2(example)
    p2(input)
if __name__ == '__main__':
    main()
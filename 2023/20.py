import time
from collections import deque

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
    timeToConj = {mod: {} for mod in modType.keys()}
    for mod in modDest.keys():
        for dest in modDest.get(mod):
            if dest in conjPre.keys():
                conjPre[dest][mod] = 0
                timeToConj[dest][mod] = 0 if modType[dest] == '&' else 1
            

    
    finalMod = 'rx'
    finalModDad = 'ns'
    buttonPresses = 0
    print(timeToConj)
    while not all(conjPre['ns'].values()):
        # break
        pulses = deque()
        pulses.append((0, 'broadcaster', 'broadcaster'))
        while pulses:
            if buttonPresses % 1000000 == 0:
                print(buttonPresses)
                print(timeToConj[finalModDad])
            pulseVal, mod, sender = pulses.popleft()
            # print(f'{sender} -{"high" if pulseVal else "low"}-> {mod}')
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
                if all(value > 0 for value in timeToConj[mod].values()) and timeToConj[mod] != {}:
                    t = buttonPresses
                    for v in timeToConj[mod].values():
                        t *= v
                    for m in timeToConj:
                        for v in timeToConj[m]:
                            if v == mod:
                                timeToConj[m][v] = t
                    buttonPresses = t 
                    retP = 0
                for dest in modDest[mod]:
                    pulses.append((retP, dest, mod))
            buttonPresses += 1
    return buttonPresses

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 20/puzzle_input/example.txt" if ex else "2023/day 20/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
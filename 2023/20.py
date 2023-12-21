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
    nameType, recievesFrom, destinations = {}, {}, {}
    for line in input:
        cur, dest = line.split('->')
        if cur[0] == 'b':
            # broadcaster
            nameType.update({cur[0:-1]: (cur[0:-1], 0)})
        else:
            nameType.update({cur[1:-1]: (cur[0], 0)})
        if cur[0] == '&':
            # conjuction
            recievesFrom.update({cur[1:-1] : {}})
        destinations.update({cur[1:-1] if cur[0] != 'b' else cur[0:-1]: [ch.strip() for ch in dest.strip().split(',')]})
    
    for conj in recievesFrom.keys():
        for dest in destinations.keys():
            if conj in destinations.get(dest):
                recievers = recievesFrom.get(conj)
                print(recievers)
                recievers.update({dest:0})
                recievesFrom.update({conj: recievers})
    print(f'{nameType}, {recievesFrom}, {destinations}')  

    pulse = 0
    seen = []
    current = 'broadcaster'  
    state = ()
    queue = deque()
    queue.append(current)
    while queue:
        print(queue)
        current = queue.popleft()
        out = [nameType.get(i)[1] if nameType.get(i) else 0 for i in destinations.get(current)]
        state = (current, out)
        if state in seen:
            print(seen)
            break
        
        seen.append(state)
        
        for dest in destinations.get(current):
            if not nameType.get(dest):
                continue
            modType, onOrOff = nameType.get(dest)
            retPulse = -1
            if modType == '%':
                if pulse == 0:
                    nameType.update({dest:(modType, not onOrOff)})
                    retPulse = 1 if onOrOff else 0
            if modType == '&':
                new = recievesFrom.get(dest)
                new.update({current:pulse})
                recievesFrom.update({dest:new})
                if all(recievesFrom.values()):
                    retPulse = 0
                else:
                    retPulse = 1
            if modType == 'b':
                retPulse = pulse
            queue.append(dest)
            
        # got to write retpulse properly here



# Flip-flop modules (prefix %) are either on or off; they are initially off. If a flip-flop module receives a high pulse, 
# it is ignored and nothing happens. However, if a flip-flop module receives a low pulse, it flips between on and off. 
# If it was off, it turns on and sends a high pulse. If it was on, it turns off and sends a low pulse.

# Conjunction modules (prefix &) remember the type of the most recent pulse received from each of their connected input modules; 
# they initially default to remembering a low pulse for each input. When a pulse is received, the conjunction module first updates 
# its memory for that input. Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.

# There is a single broadcast module (named broadcaster). When it receives a pulse, it sends the same pulse to all of its destination modules.

    print(state)
    return 

@execute
def p2(input):
    return

# when called from ~/Code/repos/advent_of_code$
ex = 1
input = open("2023/day 20/puzzle_input/example2.txt" if ex else "2023/day 20/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
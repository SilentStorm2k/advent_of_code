import time
import sympy

def execute(func):
    def wrapper(*args):   
        t1 = time.time()
        print(f'Answer for {func.__name__} : {func(*args)}')
        t2 = time.time()
        print(f'Executed in : {round(t2-t1, 5)}')
    wrapper.__original = func # if need to reuse p1 w/o decorator use : p1.__original(input)
    return wrapper 

@execute
def p1(input, bounds=(200000000000000,400000000000000)):
    pos_vel = set()
    input = input.split('\n')
    for row in input:
        a, b = row.strip().split('@')
        a = tuple([int(i) for i in a.strip().split(',')])
        b = tuple([int(i) for i in b.strip().split(',')])
        pos_vel.add((a,b))
    # print(len(pos_vel))
    pos_vel = sorted(pos_vel)
    # print(pos_vel)
    answer = 0
    destroyed = {pos: [] for pos in pos_vel}
    for i in range(len(pos_vel)):
        for j in range(i+1, len(pos_vel)):
            (x1, y1, z1), (vx1, vy1, vz1) = pos_vel[i]
            (x2, y2, z2), (vx2, vy2, vz2) = pos_vel[j]  
            a1 = vy1
            b1 = -vx1
            c1 = a1*x1 + b1*y1
            a2 = vy2
            b2 = -vx2
            c2 = a2*x2 + b2*y2      
            determinant = a1*b2 - a2*b1
            if (determinant != 0):
                x = (b2*c1 - b1*c2)/determinant
                y = (a1*c2 - a2*c1)/determinant
                if bounds[0]<=x<=bounds[1] and bounds[0]<=y<=bounds[1]: # and pos_vel[i] not in destroyed and pos_vel[j] not in destroyed:
                    answer += 1
                    # check if collision was forward in time
                    if (x-x1)/vx1 > 0 and (y-y1)/vy1 > 0 and (x-x2)/vx2 > 0 and (y-y2)/vy2 > 0:
                        # at destroyed[pos(x)] we store : steps away from collision, what its colliding with, and where its colliding at
                        destroyed[pos_vel[i]].append(((x-x1)/vx1, pos_vel[j], pos_vel[i], (x,y)))
                        destroyed[pos_vel[j]].append(((x-x2)/vx2, pos_vel[i], pos_vel[j], (x,y)))
    s = 0
    inTime = []
    for d in destroyed.keys():
        sor = sorted(destroyed[d])
        inTime.append(sor)
        destroyed.update({d:sor})
        s += len(destroyed[d])
    inTimeFlat = [element for sublist in inTime for element in sublist]
    inTimeFlat = sorted(inTimeFlat)
    answer = len(inTimeFlat)/2
    alreadyDestroyed  = set()
    collis = 0
    for ele in inTimeFlat:
        h1, h2, col = ele[1], ele[2], ele[3]
        if h1 in alreadyDestroyed and h2 in alreadyDestroyed:
            continue
        else:
            collis += 1
            alreadyDestroyed.add(h1)
            alreadyDestroyed.add(h2)
    

    return answer

@execute
def p2(input):
    pos_vel = set()
    input = input.split('\n')
    for row in input:
        a, b = row.strip().split('@')
        a = tuple([int(i) for i in a.strip().split(',')])
        b = tuple([int(i) for i in b.strip().split(',')])
        pos_vel.add((a,b))
    pos_vel = sorted(pos_vel)
    answer = 0

    xr, yr, zr, vxr, vyr, vzr = sympy.symbols('xr, yr, zr, vxr, vyr, vzr')
    equations = []
    for pos in pos_vel:
        sx, sy, sz = pos[0]
        vx, vy, vz = pos[1]
        equations.append((xr-sx)*(vy-vyr) - (yr-sy)*(vx-vxr))
        equations.append((yr-sy)*(vz-vzr) - (zr-sz)*(vy-vyr))
        
        answers = [soln for soln in sympy.solve(equations) if all(x%1==0 for x in soln.values())]

    print(len(answers))
    answer = answers[0][xr] + answers[0][yr] + answers[0][zr]

    return answer

# when called from ~/Code/repos/advent_of_code$
ex = 0
input = open("2023/day 24/puzzle_input/example.txt" if ex else "2023/day 24/puzzle_input/input.txt", 'r').read()
p1(input)
p2(input)
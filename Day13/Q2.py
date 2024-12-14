def solve(A:tuple,B:tuple,goal:tuple)->tuple:
    eq1 = [A[0],B[0],goal[0]]
    eq2 = [A[1],B[1],goal[1]]
    m1 = eq2[0]
    m2 = eq1[0]
    for i in range(3):
        eq1[i] *= m1
        eq2[i] *= m2
    y = [eq1[1] - eq2[1],eq1[2] - eq2[2]]
    y = y[1]//y[0]
    x = (goal[0]-B[0]*y)//A[0]
    return x,y

def validate(A:tuple,B:tuple,goal:tuple,solution:tuple)->bool:
    eq1 = [A[0]*solution[0],B[0]*solution[1],goal[0]]
    eq2 = [A[1]*solution[0],B[1]*solution[1],goal[1]]
    return eq1[0]+eq1[1] == eq1[2] and eq2[0]+eq2[1] == eq2[2]

def tokensSpent(buttons:tuple)->int:
    return buttons[0]*3+buttons[1]

file = open("input.txt","r")
rules = file.read().strip().split("\n\n")
allMachines = []
for game in range(len(rules)):
    x = rules[game].split("\n")
    values = []
    for i in x:
        offset = 10000000000000
        _, curr = i.split(": ")
        curr = curr.split(", ")
        machine = (int(curr[0][2:]),int(curr[1][2:]))
        values.append(machine)
    values[2] = (values[2][0]+offset,values[2][1]+offset)
    allMachines.append(values)

tokens = 0
for i in allMachines:
    solution = solve(*i)
    if validate(*i,solution):
        tokens+=tokensSpent(solution)
print(tokens)

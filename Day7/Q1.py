
# helper functions
def createCombinations(equation):
    operators = len(equation)-1
    combo = [0]*operators
    return combo

def iterateCombo(combo):
    curr = len(combo)-1
    while curr>=0:
        combo[curr]+=1
        if curr==0:
            return
        if combo[curr] <= 1:
            return
        else:
            combo[curr] = combo[curr]%2
            curr-=1
    return

def testCombo(equation,combo):
    # [+,*] operation order
    test = equation[0]
    for i in range(len(combo)):
        if combo[i] == 0:
            test*=equation[i+1]
        elif combo[i] == 1:
            test+=equation[i+1]
    return test

def validate(test,real):
    return test==real

# import the data
file = open("input.txt","r")
equations = file.read().strip().split("\n")

# split each equation 
processed = []
for i in range(len(equations)):
    total,numbers = equations[i].split(": ")
    total = int(total)
    numbers = numbers.split(" ")
    numbers = [int(i) for i in numbers]
    processed.append([total,numbers])

total = 0
counter = 0
for i in processed:
    real = i[0]
    equation = i[1]
    combo = createCombinations(equation)
    while combo[0]<=1:
        test = testCombo(equation,combo)
        if validate(test,real):
            total += real
            counter+=1
            break
        iterateCombo(combo)
print(total,counter)








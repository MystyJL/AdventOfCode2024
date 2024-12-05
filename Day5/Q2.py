def iscorrect(rules, sequence):
    # assume rules is a dictionary of what numbers come after
    current = []
    for i in sequence:
        currentRule = rules[i]
        for j in current:
            if j in currentRule:
                return False
        current.append(i)
    return True

def createGreaterRules(rawRules):
    rules = {}
    for i in rawRules:
        before,after = i.split("|")
        before = int(before)
        after = int(after)
        if before not in rules:
            rules[before] = [after]
        else:
            rules[before].append(after)
    return rules

def createLesserRules(rawRules):
    rules = {}
    for i in rawRules:
        before,after = i.split("|")
        before = int(before)
        after = int(after)
        if after not in rules:
            rules[after] = [before]
        else:
            rules[after].append(before)
    return rules

def prepareSequence(rawSequence):
    sequence = []
    for i in rawSequence:
        finished = []
        s = i.split(",")
        for j in s:
            finished.append(int(j))
        sequence.append(finished)
    return sequence

def swap(array,a,b):
    array[a],array[b] = array[b],array[a]

def selectionSort(sequence, lesserRule):
    # start sorting
    for i in range(len(sequence)):
        lowest = sequence[i]
        lowestindex = i
        currentRules = lesserRule[lowest]
        for j in range(i+1,len(sequence)):
            curr = sequence[j]
            if curr in currentRules:
                currentRules = lesserRule[curr]
                lowest = curr
                lowestindex = j
        swap(sequence,lowestindex,i)


# file reading and data processing
file = open("input.txt","r")
rules,sequence = file.read().strip().split("\n\n")
rules = rules.split("\n")
sequence = sequence.split("\n")
greaterRule = createGreaterRules(rules)
lesserRule = createLesserRules(rules)
sequence = prepareSequence(sequence)
total = 0

for i in sequence:
    if not iscorrect(greaterRule,i):
        selectionSort(i,lesserRule)
        if not iscorrect(greaterRule,i):
            print("Fuck")
        total+=i[len(i)//2]
print(total)

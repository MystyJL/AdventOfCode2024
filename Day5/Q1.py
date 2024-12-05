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

def createRules(rawRules):
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

def prepareSequence(rawSequence):
    sequence = []
    for i in rawSequence:
        finished = []
        s = i.split(",")
        for j in s:
            finished.append(int(j))
        sequence.append(finished)
    return sequence


file = open("input.txt","r")
rules,sequence = file.read().strip().split("\n\n")
rules = rules.split("\n")
sequence = sequence.split("\n")
RULES = createRules(rules)
SEQUENCE = prepareSequence(sequence)
total = 0
for i in SEQUENCE:
    if iscorrect(RULES,i):
        total += i[len(i)//2] 
print(total)
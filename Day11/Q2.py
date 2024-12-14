#  helper functions
def rules(number):
    if number == 0:
        return [1]
    inter = str(number)
    if len(inter)%2 == 0:
        return [int(inter[:len(inter)//2]), int(inter[len(inter)//2:])]
    else:
        return [number*2024]
    

def Q1(stones):
    for i in range(20):
        temp = []
        for j in range(len(stones)):
            result = rules(stones[j])
            for l in result:
                temp.append(l)
        stones = temp
    return len(temp)

def calc50(number):
    stones = [number]
    for i in range(20):
        temp = []
        for j in range(len(stones)):
            result = rules(stones[j])
            for l in result:
                temp.append(l)
        stones = temp
    total = 0
    for i in stones:
        if i not in countGlobe:
            countGlobe[i] = Q1([i])
        total+=countGlobe[i]
    return total
# file reading
max = 0
file = open("input.txt","r")
stones = file.read().strip().split(" ")
stones = [int(x) for x in stones]

# main
countGlobe = {}
top50 = {}
for i in range(10):
    countGlobe[i] = Q1([i])
for i in range(35):
    temp = []
    for j in range(len(stones)):
        result = rules(stones[j])
        for l in result:
            temp.append(l)
    stones = temp
total = 0
counter = 0
for i in stones:
    if i not in top50:
        top50[i] = calc50(i)
    total+=top50[i]
print(total)

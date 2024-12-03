def isSafe(report):
    increase = False
    decrease = False
    if len(report) <= 0:
        return 0
    for i in range(1,len(report)):
        diff = report[i]-report[i-1]
        if diff == 0:
            return -1
        elif diff > 0:
            increase = True
        elif diff < 0:
            decrease = True
        if abs(diff) > 3:
            return -1
        if increase and decrease:
            return -1
    return 1

def removeIndex(array,index):
    if index == -1 or index == len(array)-1:
        return array[:-1]
    elif index == 0:
        return array[1:]
    else:
        return array[:index]+array[index+1:]
file = open("input.txt","r")
data = file.read()
lines = data.split("\n")
safe = 0
for line in lines:
    numbers = line.split(" ")
    if len(numbers) > 1:
        clean = [int(numbers[i]) for i in range(len(numbers))]
        result = isSafe(clean)
        if result == -1:
            res = []
            for i in range(len(clean)):
                res.append(isSafe(removeIndex(clean,i)))
            res.append(0)
            result = max(res)
        safe+=result
print(safe)


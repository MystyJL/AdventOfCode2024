#  helper functions
def rules(number):
    if number == 0:
        return [1]
    inter = str(number)
    if len(inter)%2 == 0:
        return [int(inter[:len(inter)//2]), int(inter[len(inter)//2:])]
    else:
        return [number*2024]
    
# file reading
max = 0
file = open("input1.txt","r")
stones = file.read().strip().split(" ")
stones = [int(x) for x in stones]
prev = len(stones)
for i in range(25):
    temp = []
    for j in range(len(stones)):
        result = rules(stones[j])
        for l in result:
            temp.append(l)
    stones = temp
print(len(temp))

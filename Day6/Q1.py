def findGuard(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^":
                return [i,j]

file = open("input.txt","r")
map = file.read().strip().split("\n")
for i in range(len(map)):
    map[i] = list(map[i]) 
movement = [(-1,0),(0,1),(1,0),(0,-1)]

# find the guard
direction = 0
coord = findGuard(map)
while coord[0]>=0 and coord[0]<len(map) and coord[1]>=0 and coord[1]<len(map[0]):
    # can the guard move forward
    forward = [coord[0]+movement[direction][0], coord[1]+movement[direction][1]]
    if forward[0]>=0 and forward[0]<len(map) and forward[1]>=0 and forward[1]<len(map[0]):
        if map[forward[0]][forward[1]] == "#":
            direction+=1
            direction = direction%4
        else:
            map[coord[0]][coord[1]] = "X"
            coord = forward
    else:
        map[coord[0]][coord[1]] = "X"
        coord = forward
count = 0
for i in range(len(map)):
    for j in range(len(map[0])):
        if map[i][j] == "X":
            count+=1
print(count)
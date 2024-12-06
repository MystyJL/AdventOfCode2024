def findGuard(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^":
                return [i,j]

def moving(coords,direction):
    return (coords[0]+direction[0], coords[1]+direction[1])

file = open("input.txt","r")
map = file.read().strip().split("\n")
for i in range(len(map)):
    map[i] = list(map[i]) 
movement = [(-1,0),(0,1),(1,0),(0,-1)]

# find the guard
direction = 0
coord = findGuard(map)
start = coord.copy()
while coord[0]>=0 and coord[0]<len(map) and coord[1]>=0 and coord[1]<len(map[0]):
    # can the guard move forward
    forward = moving(coord,movement[direction])
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

Xcoords = []
for i in range(len(map)):
    for j in range(len(map[0])):
        if [i,j] == start:
            continue
        elif map[i][j] == "X":
            Xcoords.append((i,j))
loops = 0
for i in Xcoords:
    visited = set()
    coord = start
    direction = 0
    map[i[0]][i[1]] = "#"
    
    while coord[0]>=0 and coord[0]<len(map) and coord[1]>=0 and coord[1]<len(map[0]):
        # can the guard move forward
        forward = moving(coord,movement[direction])
        if forward[0]>=0 and forward[0]<len(map) and forward[1]>=0 and forward[1]<len(map[0]):
            if map[forward[0]][forward[1]] == "#":
                id = (forward,direction)
                if id in visited:
                    loops+=1
                    break
                else:
                    visited.add(id)
                direction+=1
                direction = direction%4
            else:
                map[coord[0]][coord[1]] = "X"
                coord = forward
        else:
            map[coord[0]][coord[1]] = "X"
            coord = forward
    map[i[0]][i[1]] = "X"
print(loops)
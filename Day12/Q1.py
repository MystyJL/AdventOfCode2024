# helper functions

# check how many edges
def edges(array:list, origin:tuple, stack:list)->int:
    perimeter = 0
    character = valueInarray(array, origin)
    directions = ((1,0),(0,1),(-1,0),(0,-1))
    for i in directions:
        newDir = addCoords(origin, i)
        if isEdge(array, newDir, character):
            perimeter+=1
        elif valueInarray(array, newDir) == character:
            stack.append(newDir)
    return perimeter

def isEdge(array:list, coord:tuple, character:str)->bool:
    return coord[0]<0 or coord[0]>=len(array) or coord[1]<0 or coord[1]>=len(array[0]) or valueInarray(array, coord) !=character

def addCoords(coord:tuple, direction:tuple)->tuple:
    return coord[0]+direction[0], coord[1]+direction[1]

def valueInarray(array:list, position:tuple)->str:
    return array[position[0]][position[1]]

# find perimeter and area
def perimeterAndArea(array:list, visited:set, origin:tuple)->tuple:
    if origin in visited:
        return (0,0)
    originalValue = valueInarray(array,origin)
    stack = [origin]
    perimeter = 0
    area = 0
    while len(stack)>0:
        curr = stack.pop()
        currValue = valueInarray(array,curr)
        if curr in visited:
            continue
        if currValue == originalValue:
            visited.add(curr)
            area+=1
            perimeter+=edges(array,curr,stack)
    return perimeter, area

# read file
file = open("test.txt","r")
garden = file.read().strip().split("\n")

# main
price = 0
visited = set()
for i in range(len(garden)):
    for j in range(len(garden[0])):
        p,a = perimeterAndArea(garden, visited, (i,j))
        price+= p*a
print(price)
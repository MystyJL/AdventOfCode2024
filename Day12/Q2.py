# helper functions

# check how many edges
def edges(array:list, origin:tuple, stack:list, character:str, perimeter:dict)->None:
    directions = ((1,0),(0,1),(-1,0),(0,-1))   
    for i, direction in enumerate(directions):
        # if i == 2 and character =="C":
        #     print((direction,origin[side]), (direction,origin[side]) in perimeter)
        newDir = addCoords(origin, direction)
        side = i%2 != 0 
        if isEdge(array, newDir, character):
            edge = (direction,origin[side])
            if edge not in perimeter:
                perimeter[edge] = [{origin[not side]}]
            else:
                createNew = False
                for i in range(len(perimeter[edge])):
                    positive = origin[not side]+1
                    negative = origin[not side]-1
                    if positive in perimeter[edge][i] or negative in perimeter[edge][i]:
                        perimeter[edge][i].add(origin[not side])
                        break
                    elif i == len(perimeter[edge])-1:
                        # print("fuck")
                        createNew = True
                if createNew:
                    perimeter[edge].append({origin[not side]})                    
        elif valueInarray(array, newDir) == character:
            stack.append(newDir)

def fix(array):
    if len(array) ==1:
        return array
    new = []
    while len(array)>0:
        a1 = array[0]
        i = 1
        while i<len(array):
            a2 = array[i]
            for j in a2:
                if j+1 in a1 or j-1 in a1:
                    a1 = a1.union(a2)
                    array.pop(i)
                    i-=1
                    break
            i+=1
        new.append(array.pop(0))

    return new
    

def isEdge(array:list, coord:tuple, character:str)->bool:
    return coord[0]<0 or coord[0]>=len(array) or coord[1]<0 or coord[1]>=len(array[0]) or valueInarray(array, coord) !=character

def addCoords(coord:tuple, direction:tuple)->tuple:
    return coord[0]+direction[0], coord[1]+direction[1]

def valueInarray(array:list, position:tuple)->str:
    return array[position[0]][position[1]]

# find perimeter and area
def perimeterAndArea(array:list, visited:set, origin:tuple, direction:int)->tuple:
    if origin in visited:
        return (0,0)
    originalValue = valueInarray(array,origin)
    stack = [origin]
    perimeter = {}
    area = 0
    while len(stack)>0:
        curr = stack.pop(direction)
        currValue = valueInarray(array,curr)
        if curr in visited:
            continue
        if currValue == originalValue:
            visited.add(curr)
            area+=1
            edges(array,curr,stack,originalValue,perimeter)
    numberOfSides = 0
    for i,j in perimeter.items():
        # print(len(perimeter))
        perimeter[i] = fix(perimeter[i])
        numberOfSides+=len(perimeter[i])
        
    return numberOfSides, area

# read file
file = open("test.txt","r")
garden = file.read().strip().split("\n")

# main
price = 0
price1 = 0
visited = set()
visited1= set()
for i in range(len(garden)):
    for j in range(len(garden[0])):
        p,a = perimeterAndArea(garden, visited, (i,j), 0)
        price+= p*a
        x,y = perimeterAndArea(garden, visited1, (i,j), -1)
        price1+=x*y
print(price, price1)
# helper functions
def depthFirstSearch(topography, coord):
    visited = set()
    nines = set()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    planning = [coord]
    while len(planning)>0:
        curr = planning.pop()
        visited.add(curr)
        character = currentChar(topography,curr)
        if character == 9:
            nines.add(curr)
        else:
            for i in directions:
                next = addCoords(curr,i)
                if inbounds(topography,next) and currentChar(topography,next) == character+1 and next not in visited:
                    planning.append(next)
    return len(nines)

def inbounds(topography,coord):
    return coord[0]>=0 and coord[0]<len(topography) and coord[1]>=0 and coord[1]<len(topography[0])

def currentChar(topography,coord):
    return topography[coord[0]][coord[1]]

def addCoords(coord1,coord2):
    return (coord1[0]+coord2[0],coord1[1]+coord2[1])




# file reading
file = open("input.txt","r")
topography = file.read().strip().split("\n")
for i in range(len(topography)):
    topography[i] = [int(x) for x in topography[i]]


#  main 
total = 0
for i in range(len(topography)):
    for j in range(len(topography[0])):
        curr = (i,j)
        currChar = currentChar(topography,curr)
        if currChar == 0:
            total+=depthFirstSearch(topography,curr)
print(total)
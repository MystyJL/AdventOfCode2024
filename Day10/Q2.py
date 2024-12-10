# helper functions
def breathFirstSearch(topography, coord):
    # coords:[paths,children]
    visited = [{} for i in range(0,10)]
    nines = set()
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    planning = [coord]
    while len(planning)>0:
        curr = planning.pop(0)
        children = []
        character = currentChar(topography,curr)
        if character == 9:
            visited[character][curr] = [0,None]
        elif curr not in visited[character]:
            for i in directions:
                next = addCoords(i,curr)
                if inbounds(topography,next) and currentChar(topography,next) == character+1 and next not in visited[character+1]:
                    children.append(next)
                    planning.append(next)
            visited[character][curr] = [0,children]
    planning = [coord]
    visited[0][coord][0] = 1
    paths = 0
    # print(visited)
    for i in range(0,10):
        currentDict = visited[i]
        for j,k in currentDict.items():
            children = k[1]
            if i!=9:
                for l in children:
                    visited[i+1][l][0]+= visited[i][j][0]
    for i,j in visited[9].items():
        paths+= j[0]
    # print(visited)
    # print(paths)
    return paths

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
            total+=breathFirstSearch(topography,curr)
print(total)
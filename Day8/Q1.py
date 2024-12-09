# *****************************Functions**************************************

def inbounds(coord,max):
    return coord[0]>=0 and coord[0]<max[0] and coord[1]>=0 and coord[1]<max[1]

def move(coords,movement):
    return (coords[0]+movement[0], coords[1]+movement[1])








# **************************File Reading and proccessing***************************************
file = open("input.txt","r")
maps = file.read().strip().split("\n")
for i in range(len(maps)):
    maps[i] = list(maps[i])

signals = set()
locations = {}
for i in range(len(maps)):
    for j in range(len(maps[0])):
        sig = maps[i][j]
        if sig != ".":
            signals.add(sig)
            if sig not in locations:
                locations[sig] = []
            locations[sig].append((i,j))
signals = list(signals)
dimensions = (len(maps),len(maps[0]))
#***************************Main**********************************************
antinodes = set()
for i in signals:
    coords = locations[i]
    for j in range(len(coords)):
        for k in range(j+1,len(coords)):
            movement = (coords[j][0]-coords[k][0], coords[j][1]-coords[k][1])
            first = move(coords[j],movement)
            if inbounds(first,dimensions):
                antinodes.add(first)
            movement = (coords[k][0]-coords[j][0], coords[k][1]-coords[j][1])
            second = move(coords[k],movement)
            if inbounds(second,dimensions):
                antinodes.add(second)
print(len(antinodes))


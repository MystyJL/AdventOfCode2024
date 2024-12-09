# *****************************Functions**************************************
def checksum(fileSystem):
    total = 0
    counter = 0
    for i in range(len(fileSystem)):
        if fileSystem[i] == ".":
            continue
        total+=fileSystem[i]*i
        counter+=1
    return total,counter
def swap(array,a,b):
    array[a],array[b] = array[b],array[a]

def putChunk(array, start1, start2,chunkSize):
    pt2 = start2
    pt1 = start1
    for i in range(chunkSize):
        swap(array,pt2,pt1)
        pt2-=1
        pt1+=1

def scan(array, blockSize, start, limit):
    curr = start
    while curr < limit:
        gap = size(array, curr, 1)
        if array[curr] != ".":
            curr+=gap
        elif gap>=blockSize:
            return curr
        else:
            curr+=gap
    return False

def size(array,start,direction):
    s = 0
    curr = start
    last = array[curr]
    while last == array[curr]:
        s+=1
        curr+=direction
    return s



# **************************File Reading and proccessing***************************************
file = open("input.txt","r")
system = file.read().strip()
structure = []
counter = 0
for i in range(0,len(system)):
    if i%2==0:
        for j in range(int(system[i])):
            structure.append(counter)
        counter+=1
    else:
        for j in range(int(system[i])):
            structure.append(".")
#***************************Main**********************************************
pt1 = 0
pt2 = len(structure)-1
moves = set()
dupe = 0
while pt1<pt2:
    blockSize = size(structure,pt2,-1)
    if structure[pt2] == ".":
        pt2-=blockSize
    elif structure[pt2] in moves:
        dupe+=1
        pt2-=blockSize
    elif structure[pt2] != ".":
        moves.add(structure[pt2])
        scanResult = scan(structure,blockSize,0,pt2)
        if scanResult:
            putChunk(structure,scanResult,pt2,blockSize)
        pt2-=blockSize
# print(dupe)

# print(structure)

print(checksum(structure))

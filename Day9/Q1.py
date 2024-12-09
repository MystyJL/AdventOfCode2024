# *****************************Functions**************************************
def checksum(fileSystem):
    total = 0
    counter = 0
    for i in range(len(fileSystem)):
        total+=fileSystem[i]*i
        counter+=1
    return total,counter
def swap(array,a,b):
    array[a],array[b] = array[b],array[a]



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
while pt1<pt2:
    if structure[pt1] == "." and structure[pt2] != ".":
        swap(structure,pt1,pt2)
        pt2-=1
        pt1+=1
    if structure[pt1] != ".":
        pt1+=1
    if structure[pt2] == ".":
        pt2-=1
res = [i for i in structure if i != "."] 
print(checksum(res))

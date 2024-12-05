def directions(input, coords):
    # XMAS 
    top = -1
    right = 1
    bottom = 1
    left = -1
    if coords[0]<3:
        top = 0
    if coords[1]<3:
        left = 0
    if coords[0]>len(input)-4:
        bottom = 0
    if coords[1]>len(input[0])-4:
        right = 0
    return (top,right,bottom,left)

def find(input,coords):
    counter = 0
    target = "XMAS"
    searchSpace = directions(input,coords)
    directional = (((1,0),(1,1)),((0,1),(1,1)))
    for i in range(4):
        pair = (searchSpace[i],searchSpace[(i+1)%4]) if i%2==0 else (searchSpace[(i+1)%4],searchSpace[i])
        for j in directional[i%2]:
            # no over counting
            if j == (1,1) and (pair[0] == 0 or pair[1] == 0):
                break 
            reset = coords.copy()
            # loop to check for XMAS
            correct = 0
            for k in range(4):
                if input[reset[0]][reset[1]] != target[k]:
                    break
                elif input[reset[0]][reset[1]] == target[k]:
                    correct+=1
                else:
                    print("Fuck")
                reset[0]+= pair[0]*j[0]
                reset[1]+= pair[1]*j[1]
            if correct == 4:
                counter+=1
    return counter

def onestar():
    file = open("input.txt","r")
    wordsearch = file.read().strip()
    wordsearch = wordsearch.split("\n")
    xmas = 0
    for i in range(len(wordsearch)):
        for j in range(len(wordsearch[0])):
            if wordsearch[i][j] == "X":
                xmas+=find(wordsearch,[i,j])
    print(xmas)
onestar()

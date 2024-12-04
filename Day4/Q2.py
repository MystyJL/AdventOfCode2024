def find(input,coords):
    if coords[0]<1 or coords[1]<1 or coords[0]>len(input)-2 or coords[1]>len(input)-2:
        return 0
    counter = {"M":0,"S":0}
    directions = ((-1,-1),(1,1),(-1,1),(1,-1))
    topLeft = coords.copy()
    topLeft[0] += -1
    topLeft[1] += -1
    bottomRight = coords.copy()
    bottomRight[0] += 1
    bottomRight[1] += 1
    if input[topLeft[0]][topLeft[1]] == input[bottomRight[0]][bottomRight[1]]:
        return 0
    for i in directions:
        reset = coords.copy()
        reset[0]+=i[0]
        reset[1]+=i[1]
        letter = input[reset[0]][reset[1]]
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter]+=1
    if counter["M"] == 2 and counter["S"] == 2:
        return 1

    
    return 0


file = open("input.txt","r")
wordsearch = file.read().strip()
wordsearch = wordsearch.split("\n")
xmas = 0
for i in range(len(wordsearch)):
    for j in range(len(wordsearch[0])):
        if wordsearch[i][j] == "A":
            xmas+=find(wordsearch,[i,j])
print(xmas)

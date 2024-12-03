file = open("input.txt","r")
data = file.read()
def do(input,index):
    string = "do()"
    counter = 0
    if index+3 > len(input):
        return -1
    for i in range(0,4):
        if input[index+i] != string[i]:
            break
        elif input[index+i] == string[i]:
            counter+=1
    if counter == 4:
        return 1
    string = "don't()"
    counter = 0
    for i in range(0,7):
        if input[index+i] != string[i]:
            break
        elif input[index+i] == string[i]:
            counter+=1
    if counter == 7:
        return 2
    else:
        return -1
    
def isInstruction(input, index):
    string = "mul(?,?)"
    counter = 0
    d1 = ["",False]
    d2 = ["",False]
    i = index
    while i<len(input) and counter<8:
        if string[counter] == "?":
            if input[i].isdigit() and not d1[1]:
                d1[0]+=input[i]
                i+=1
            elif input[i].isdigit() and d1[1]:
                d2[0]+=input[i]
                i+=1
            elif not input[i].isdigit() and not d1[1]:
                counter+=1
                d1[1] = True
            elif not input[i].isdigit() and d1[1]:
                counter+=1
                d2[1] = True
        elif string[counter] == input[i]:
            i+=1
            counter+=1
        else:
            return 0
    if counter>=7:
        return d1[0],d2[0]
    else:
        return 0
total = 0
enabled = True
for i in range(len(data)):
    if data[i] == "m" and enabled:
        numbers = isInstruction(data,i)
        if numbers != 0 and len(numbers[0])<=3 and len(numbers[1])<=3:
            total+=int(numbers[0])*int(numbers[1])
    if data[i] == "d":
        numbers = do(data,i)
        if numbers == 1:
            enabled = True
        elif numbers == 2:
            enabled = False
print(total)


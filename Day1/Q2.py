file = open("input.txt","r")
text = file.read()
lines = text.split("\n")
left = []
right = {}
for line in lines:
    numbers = line.split("   ")
    if len(numbers) == 2:
        left.append(int(numbers[0]))
        r = int(numbers[1])
        if r not in right:
            right[r] = 1
        else:
            right[r]+=1
similarity = [left[i]*right[left[i]] for i in range(len(left)) if left[i] in right]
sum(similarity)
print(sum(similarity))
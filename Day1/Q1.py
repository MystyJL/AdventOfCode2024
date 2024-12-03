file = open("input.txt","r")
text = file.read()
lines = text.split("\n")
left = []
right = []
for line in lines:
    numbers = line.split("   ")
    if len(numbers)==2:
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))
left.sort()
right.sort()
differences = [abs(left[i]-right[i]) for i in range(len(left))]
print(differences)
print(sum(differences))

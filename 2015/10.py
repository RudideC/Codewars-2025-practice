val = [input()]

while val[-1] != val[0] or len(val) == 1:
    val.append(input())

val.pop(-1)

for i in range(int(len(val)/2) + 1): # Unsure if this is correct, would need more test cases to make sure
    print(val[0], end="; ")
    print(val[i + 1], end="; ")
    print(val[i + 2])

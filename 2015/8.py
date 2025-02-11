numbers = []

for i in range(0, 256):
    numbers.append(0)

dimensions = input()

dimensions = dimensions.split(" ")
height = dimensions[0]

for i in range(int(height) - 1):
    row = input()
    nums = row.split(" ")
    for num in nums:
        numbers[int(num)] += 1

# Don't know how, but this works
for i in range(0, 256):
    if i == 1 or i == 0:
        print(numbers[i], end=" ")
    elif ((i + 1) % 16) != 0:
        print(numbers[i], end=" ")
    else:
        print(numbers[i], end="\n")
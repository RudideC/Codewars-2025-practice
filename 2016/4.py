nums = [input()]
while nums[-1] != "0":
    nums.append(input().strip())

nums.pop(-1)

for num in nums:
    count_even = 0
    count_odd = 0
    numl = list(num)
    for i in range(len(numl)):
        if i % 2:
            count_even += int(numl[i])
        else:
            count_odd += int(numl[i])
    if count_odd == count_even:
        print(f"{num} is a balanced number")
    else:
        print(f"{num} is not a balanced number")
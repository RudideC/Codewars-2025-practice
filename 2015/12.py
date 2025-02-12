nums = [input()]
while nums[-1] != "0":
    nums.append(input())
    
nums.pop(-1)

balance = float(nums[0])

for i in range(1, len(nums)):
    if not float(nums[i]) % 5:
        if balance - float(nums[i]) - 0.5 >= 0:
            balance = balance - float(nums[i]) - 0.50
    print(f"{nums[i]} {float(balance):.2f}")
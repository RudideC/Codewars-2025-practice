n = int(input())
m = int(input())

total = 0
total2 = 0

for i in range(1, m + 1):
    total += n + i

for i in range(1, m + 1):
    total2 += n - i

print(total, total2)
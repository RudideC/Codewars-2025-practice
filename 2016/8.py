n, e = input().split(" ")

a = []

for i in range(int(e)):
    total = 0
    if len(a) < int(n):
        total = 1
    else:
        for p in a:
            total += p
        a.pop(0)

    a.append(total)
    print(total, end=" ")

print()
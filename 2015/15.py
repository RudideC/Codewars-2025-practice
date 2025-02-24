n = int(input())

a = []

events = []

for i in range(n):
    a.append(input())

for i in range(len(a)):
    one, two = a[i].split(" ")
    events.append((int(one), 1))
    events.append((int(two), -1))


events.sort()

needed = 0
current = 0

for event in events:
    current += event[1]
    needed = max(needed, current)

print(needed)
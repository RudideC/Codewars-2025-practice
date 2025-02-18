numbers = [input()]
while numbers[-1] != "0":
    numbers.append(input().strip())

numbers.pop(-1)

d = {}

for num in numbers:
    a = num.split(" ")
    if a[0] not in d:
        d[a[0]] = 0
    if a[1] not in d:
        d[a[1]] = 0
    if a[2] not in d:
        d[a[2]] = 0
    d[a[0]] += 3
    d[a[1]] += 2
    d[a[2]] += 1

# The lambda thing makes it sort by value instead of key
sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
top_3 = sorted_items[:3]

for key, value in top_3:
    print(key, value)
a = []
a.append(input().strip())
while a[-1] != ".":
    a.append(input().strip())
a.pop(-1)
f = {}

for i in a:
    name, d, s = i.split(" ")
    f[name] = int(int(d)/int(s))

f = sorted(f.items(), key=lambda x: x[1])
for e in f:
    print(e[0], e[1])
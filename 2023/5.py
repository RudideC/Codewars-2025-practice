vowels = ["a", "e", "i", "o", "u"]

line = list(input())

for l in line:
    if l.lower() in vowels:
        l = "*"
    print(l, end="")

print()
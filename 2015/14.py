values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def romanToArabic(roman):
    t = list(roman)
    for i in range(len(t)):
        t[i] = values[t[i]]
    total = 0
    prev_value = 0
    for val in reversed(t):
        if val < prev_value:
            total -= val
        else:
            total += val
        prev_value = val

    return total

a = []
a.append(input())
while a[-1] != ".":
    a.append(input().strip())

a.pop(-1)

for ix in a:
    print(romanToArabic(ix))
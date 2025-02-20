def numToBinary(num) -> list:
    a = []
    t = [8, 4, 2, 1]
    num = int(num)
    for i in t:
        if num == 0:
            break
        if num >= i:
            a.append("o")
            num -= i
        else:
            a.append("-")
    while len(a) < 4:
        a.append("-")
    return a

time = input()
time = time.split(":")
h1, h2 = list(time[0])
m1, m2 = list(time[1])
s1, s2 = list(time[2])

h1, h2, m1, m2, s1, s2 = numToBinary(h1), numToBinary(h2), numToBinary(m1), numToBinary(m2), numToBinary(s1), numToBinary(s2)
for i in range(0, 4):
    print(h1[i], h2[i], m1[i], m2[i], s1[i], s2[i])
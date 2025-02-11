# Not the most optimal solution
#? The input/output shown in this question seems incorrect
def pair(letter) -> str:
    if letter.lower() == "a":
        return "T"
    elif letter.lower() == "c":
        return "G"
    elif letter.lower() == "g":
        return "C"
    elif letter.lower() == "t":
        return "A"

def reverse(e) -> None:
    for u in e:
        print(pair(u), end="")
    print()

a = []
a.append(input())
while a[-1] != ".":
    a.append(input())

for i in range(len(a) - 1):
    reverse(list(a[i]))
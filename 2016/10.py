# Overcomplicated ahh solution
text = input().strip()

text = text.split(".")
if text[-1] == "":
    text.remove("")

for t in text:
    t = t.strip()
    e = t.split(" ")
    print(e[0], end="")
    for i in range(1, len(e)):
        if e[i].lower() == "i":
            e[i] = "I"
        else:
            e[i] = e[i].lower()
        print(f" {e[i]}", end="")
    print("." ,end=" ")
print()
gender = input()
size = input()
size = float(size)
if gender == "M":
    if size >= 44:
        size -= 35
    else:
        size -= 34.5
elif gender == "F":
    if size >= 40:
        size -= 32
    else:
        size -= 31.5
print(size)

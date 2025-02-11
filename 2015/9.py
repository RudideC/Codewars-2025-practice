file_path = input()

f = open(file_path, "r")

text = f.read()

lines = text.split("\n")

for line in lines:
    if line == "": # Empty line
        continue
    a = list(line)
    print(line[0], end = "")

print()
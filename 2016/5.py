records = [input()]
while records[-1] != "#":
    records.append(input().strip())

records.pop(-1)

w = 0
z = 0

for rec in records:
    rec = rec.split(" ")
    if int(rec[1]) > int(rec[2]):
        if rec[0] == "W":
            w += 1
        else:
            z += 1

print(f"{w} fines to Whynot")
print(f"{z} fines to Zzyzx")
if w < z:
    print("Whynot inhabitants are safer at driving than Zzyzx ones")
elif z < w:
    print("Zzyzx inhabitants are safer at driving than Whynot ones")
else:
    print("Whynot and Zzyzx inhabitants are equally safe at driving")
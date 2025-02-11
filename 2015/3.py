age = input()
name = input()
if int(age) <= 2:
    ageHuman = 10 * int(age)
else:
    ageHuman = 20 + (int(age) - 2) * 4
print(f"{name} is {ageHuman} human years old")
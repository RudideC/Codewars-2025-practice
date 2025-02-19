total = int(input())
first = input()
first = first.split(" ")
second = input()
second = second.split(" ")

magic = total - int(first[1]) - int(second[2]) + 1

print(f"{first[0]} must win {magic} matches")

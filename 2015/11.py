sizes = input()
sizes = sizes.split(" ")

nums = [input()]
while nums[-1] != "0":
    nums.append(input())

nums.pop(-1)

if "1" not in sizes:
    sizes.insert(0, "1")

sizes.reverse() # Sizes in descending order

for num in nums:
    a = int(num)
    print(f"{a} litres require", end=" ")
    for size in sizes:
        if a - int(size) < 0:
            continue
        else:
            t = int(a / int(size))
            a = a - (t * int(size))
            print(f"{t} jar(s) of {size}", end="")
            if a != 0:
                print(",", end=" ")
            else:
                break
    print()


    

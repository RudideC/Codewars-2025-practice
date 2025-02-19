e = int(input())

o = ["0 0"]

for i in range(e):
    o.append(input().strip())

for i in range(1, len(o)):
    currX, currY = o[i].split(" ")
    prevX, prevY = o[i - 1].split(" ")
    currX, currY, prevX, prevY = int(currX), int(currY), int(prevX), int(prevY) # Yeah
    if currY < prevY:
        print(f"Walk {prevY - currY} steps south")
    elif currY > prevY:
        print(f"Walk {currY - prevY} steps north")
    if currX < prevX:
        print(f"Walk {prevX - currX} steps west")
    elif currX > prevX:
        print(f"Walk {currX - prevX} steps east")
side1 = int(input())
side2 = int(input())
side3 = int(input())

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("It is a triangle")
else:
    print("It is NOT a triangle")
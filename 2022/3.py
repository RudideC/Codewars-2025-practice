products = int(input())
boxes = int(input())
left = int(input())

if products % boxes == left:
    print(f"CORRECT, the capacity of each box is {int(products/boxes)}") # Don't know if rounding is needed, but just makes sense
else:
    print("INCORRECT")
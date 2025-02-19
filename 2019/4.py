run = True

if int(input()) < 5:
    run = False
if int(input()) < 2:
    run = False
if int(input()) < 50:
    run = False

if run:
    print("You can run the game")
else:
    print("You can NOT run the game")
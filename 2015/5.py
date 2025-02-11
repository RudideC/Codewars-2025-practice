def checkPalindrome(phrase) -> bool:
    phrase = phrase.lower()
    phrase = phrase.strip()
    phrase = phrase.replace(" ", "")
    phrase = phrase.replace(",", "")
    phrase = phrase.replace(".", "")
    phrase = list(phrase)
    for i in range (int(len(phrase)/2) + 1):
        if phrase[i] != phrase[-(i + 1)]:
            return False
    return True

a = []
a.append(input())
while a[-1] != "Palindrome!":
    a.append(input())

for j in range(len(a) - 1):
    if checkPalindrome(a[j]):
        print(f'"{a[j].rstrip()}" is a palindrome')
    else:
        print(f'"{a[j].rstrip()}" is not a palindrome')     


v = ["a", "e", "i", "o", "u"] 

text = ""
while True:
    line = input()
    if '#' in line:
        text += line[:line.find('#')]
        break
    else:
        text += line + " "

text = text.replace(" ", "")
text = text.replace(",", "")
text = text.replace(".", "")
text = text.replace("'", "")
text = text.replace("-", "")
text = text.replace("?", "")
text = text.replace("!", "")
text = list(text.strip().lower())

vowels = 0

for letter in text:
    if letter in v:
        vowels += 1

consonants = len(text) - vowels

try:
    ratio = int((vowels / consonants) * 1000) / 1000
except ZeroDivisionError:
    ratio = "Infinite"

print(f"Consonants: {consonants}")
print(f"Vowels: {vowels}")
print(f"Ratio: {ratio:.3f}")

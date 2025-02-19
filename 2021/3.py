plans = {
    15: [0, "Free"],
    50: [2.99, "Occasional"],
    100: [4.99, "Moderate"],
    300: [9.99, "Frequent"],
    700: [19.99, "Business"],
}

pages = int(input())
print(f"Plan in order to print {pages} pages per month:")
if pages <= 15:
    print(f"Free.")
    print(f"Price: 0 Euros.")
elif pages <= 50:
    print("Occasional.")
    print("Price: 2.99 Euros.")
elif pages <= 100:
    print("Moderate.")
    print("Price: 4.99 Euros.")
elif pages <= 300:
    print("Frequent.")
    print("Price: 9.99 Euros.")
elif pages <= 700:
    print("Business.")
    print("Price: 19.99 Euros.")
else:
    print("Not available.")
    print("Price: - Euros.")
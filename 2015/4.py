def isPrime(num) -> bool:
    if num <= 1:
        return False
    else:
        for j in range (2, int(num ** 0.5) + 1):
            if num % j == 0:
                return False
        return True

a = []
a.append(input())
while a[-1] != '0':
    a.append(input())

for i in range (0, len(a) - 1):
    if isPrime(int(a[i])):
        print(f"{a[i]} is prime")
    else:
        print(f"{a[i]} is not prime")




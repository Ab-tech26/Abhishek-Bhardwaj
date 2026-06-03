num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    rem = num % 10
    num = num // 10

    reverse = reverse * 10 + rem
print("Reverse =", reverse)
num = int(input("Enter the number: "))

total = 0

while num > 0:
    rem = num % 10
    total += rem
    num = num // 10

print("Sum of digits =", total)
num = int(input("Enter a number: "))

status = True

num>0

for i in range(2, num):
    if num % i == 0:
        status = False
        break

if status:
    print(f"number is prime: {num}")
else:
    print(f"number is not a prime: {num}")

if num <= 0 :
    print(f"number is not a prime: {num}")

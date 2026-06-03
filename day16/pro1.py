num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

try:
    result = num1/num2
    print(f"Result is : {result};")
except ZeroDivisionError:
    print(f"Kindly do not enter second number as zero ")
    num2 = int(input("Enter second number : "))
    try:
        result = num1/num2
        print(f"Result is : {result};")
    except ZeroDivisionError:
        print(f"This is your last chance to enter the second number ")
        num2 = int(input("Enter second number : "))
        try:
            result = num1/num2
            print(f"Result is : {result};")
        except Exception:
            print("bhai tu chla ja vrna police bula lunga  ")


# print("no bro")

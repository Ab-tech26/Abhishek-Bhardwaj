try:
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    result = num1 + num2
    print(result + "300")

except ValueError:
    print("Handelling for value error")

except TypeError:
    print("Handelling for type error")





except Exception:
    print("bhai tu chla ja vrna police bula lunga  ")




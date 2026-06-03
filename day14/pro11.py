status = True
while status:
    print("""
    1. Addition
    2. Substraction
    3. Multiplication
    4. Exit
    """)

    choice = int(input("Enter your choice : "))
    if choice == 1:
        num1 = int(input("enter first number : "))
        num2 = int(input("enter second number : "))
        result = num1 + num2 
        print(f"Sum of two number is : {result}")
    elif choice==2:
        num1 = int(input("enter first number : "))
        num2 = int(input("enter second number : "))
        result = num1 - num2 
        print(f"Substraction of two number is : {result}")
    elif choice==3:
        num1 = int(input("enter first number : "))
        num2 = int(input("enter second number : "))
        result = num1 * num2 
        print(f"Multiplication of two number is : {result}")
    else:
        print("Thanks for using calculator")
        status=False
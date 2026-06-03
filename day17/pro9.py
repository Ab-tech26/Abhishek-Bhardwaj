num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

result = num1+num2

print ( f"sum of two number : {result}")

file = open("abhi.txt","w")
file.write(str(result))
file.read(str(result))
file.close()
print ( "Succcessfully ")
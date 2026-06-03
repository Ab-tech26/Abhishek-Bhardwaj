num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
num4 = int(input("Enter fourth number : "))

if num1>num2:
    if num1>num3:
        if num1>num4:
          print(f"Number 1 is greater : {num1}")
        else:
            print(f"Number 4 is greater : {num4}")
    else:
        if num3>num4:
            print(f'num 3 is greater : "{num3}')
        else:
            print (f'Number 4 is greater : {num4}')
  
else:
    if num2>num3:
        if num2>num4:
         print(f"Number 2 is greater : {num2}")
        else:
         print (f'Number 4 is greater : {num4}')
        
    else:
        if num3>num4:
            print(f'Number 3 is greater : {num3}')
           
        else:
           print(f"Number 4 is greater : {num4}")
           
        
        
        

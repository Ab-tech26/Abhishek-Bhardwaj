inputnum = input("enter a number : ")
size = len(inputnum)
num= int(inputnum)
smallest = 9
for i in range (size):
 rem = num % 10
 num = num //10

 if rem < smallest:
  smallest=rem

print("smallest digit  = ", smallest)

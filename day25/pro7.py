inputnum = input("enter a number : ")
size = len(inputnum)
num= int(inputnum)
count = 0
for i in range (size):
   num = num//10
   count+=1
print("count = ", count)

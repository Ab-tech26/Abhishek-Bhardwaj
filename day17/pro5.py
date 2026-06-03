classMarks=[1,2.3,78,100,6,77,100.2]

max=classMarks[0]
for individual_Marks in classMarks:
    if individual_Marks>max:
        max = individual_Marks
print(f'maximum marks is : {max}')
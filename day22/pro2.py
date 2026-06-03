import threading
import random


def generate_contacts(file_name,total_records):
    with open(file_name, "w") as file:
        for _ in range (total_records):
            number = random.randint(6000000000, 9999999999)

            file.write(str(number)  + "\n")

generate_contacts('contact1.txt' , 200)
generate_contacts('contact2.txt' , 200)
generate_contacts('contact3.txt' , 200)
generate_contacts('contact4.txt' , 200)

print ("files created successfully\n")



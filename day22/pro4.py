import threading
import random


# def generate_contacts(file_name,total_records):
#     with open(file_name, "w") as file:
#         for _ in range (total_records):
#             number = random.randint(6000000000, 9999999999)

#             file.write(str(number)  + "\n")

# generate_contacts('contact1.txt' , 200)
# generate_contacts('contact2.txt' , 200)
# generate_contacts('contact3.txt' , 200)
# generate_contacts('contact4.txt' , 200)

# print ("files created successfully\n")


def search_number(file_name, target_number):
    found = False
    with open(file_name, "r") as file:
        for line_no, number in enumerate(file, start=1):
            number = number.strip()

            if number ==target_number:
                print(f"{target_number} FOUND IN {file_name} at line {line_no}")
                found = True
                break
    if not found :
        print(f"{target_number} NOT FOUND IN  {file_name}")

search_contact = input("enter contact to search : ")
     
t1 = threading.Thread(
    target=search_number,
    args=("contact1.txt", search_contact)
)
t2 = threading.Thread(
    target=search_number,
    args=("contact2.txt", search_contact)
)
t3 = threading.Thread(
    target=search_number,
    args=("contact3.txt", search_contact)
)
t4 = threading.Thread(
    target=search_number,
    args=("contact4.txt", search_contact)
)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
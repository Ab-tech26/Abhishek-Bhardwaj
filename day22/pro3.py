import threading
import random



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
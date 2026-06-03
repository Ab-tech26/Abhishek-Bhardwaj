import string
import random

# def generate_password(length=6):

upper1 = (chr(random.randint(65,90)))
upper2 = (chr(random.randint(65,90)))
lower1 = (chr(random.randint(97,106)))
lower2 = (chr(random.randint(97,106)))
special1 = (chr(random.randint(32,45)))
special2 = (chr(random.randint(32,45)))

password_list = upper1 + upper2 +lower1 +lower2 +special1 + special2
random.shuffle(password_list)

print(password_list)


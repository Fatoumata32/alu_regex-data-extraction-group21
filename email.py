import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

user_input = input("Enter the email to validate: ")

if is_valid_email(user_input):
    print(f"{user_input} is a valid email.")
else:
    print(f"{user_input} is an invalid email.")

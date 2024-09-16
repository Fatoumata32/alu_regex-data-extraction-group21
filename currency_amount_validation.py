import re

def is_valid_currency(currency):
    pattern = r'^\$\d{1,3}(,\d{3})*(\.\d{2})?$'
    return re.match(pattern, currency) is not None

user_input = input("Enter the currency amount to validate: ")

if is_valid_currency(user_input):
    print(f"{user_input} is a valid currency amount.")
else:
    print(f"{user_input} is an invalid currency amount.")

import re

def phone_number_validation(phone_number):
    pattern= re.compile(r"^\+?(\d{1,3})?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})$")

    if pattern.match(phone_number):
        return True
    else:
        return False
    
# Example

phone= ["(123) 456-7890", "123-456-7890", "123.456.7890", "1234567890", "+250 123 456 7890"]

for phone_number in phone:
    print(f"{phone_number}: {phone_number_validation(phone_number)}")
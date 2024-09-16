import re

def credit_card_validation(card_number):
    pattern = re.compile(r"^(?:\d{4}[\s-]?){3}\d{4}$")
    
    if pattern.match(card_number):
        return True
    else:
        return False

# Example usage
credit_card_number = "1234-5678-9876-5432"
if credit_card_validation(credit_card_number):
    print(f"{credit_card_number} is a valid credit card number")
else:
    print(f"{credit_card_number} is not a valid credit card number")
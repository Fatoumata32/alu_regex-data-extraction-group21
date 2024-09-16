import re

def is_valid_html_tag(tag):
    pattern = r'^<\/?[a-zA-Z][a-zA-Z0-9]*\s*[^>]*>$'
    return re.match(pattern, tag) is not None

user_input = input("Enter the HTML tag to validate: ")

if is_valid_html_tag(user_input):
    print(f"{user_input} is a valid HTML tag.")
else:
    print(f"{user_input} is an invalid HTML tag.")


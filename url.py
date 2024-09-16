import re

def is_valid_url(url):
    pattern = r'^(https?:\/\/)?([a-zA-Z0-9-_]+(\.[a-zA-Z0-9-_]+)+.*)$'
    return re.match(pattern, url) is not None

user_input = input("Enter the URL to validate: ")

if is_valid_url(user_input):
    print(f"{user_input} is a valid URL.")
else:
    print(f"{user_input} is an invalid URL.")

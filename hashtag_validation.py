import re

def is_valid_hashtag(hashtag):
    pattern = r'^#[a-zA-Z0-9_]+$'
    return re.match(pattern, hashtag) is not None

user_input = input("Enter the hashtag to validate: ")

if is_valid_hashtag(user_input):
    print(f"{user_input} is a valid hashtag.")
else:
    print(f"{user_input} is an invalid hashtag.")


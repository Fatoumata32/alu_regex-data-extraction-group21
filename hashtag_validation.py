import re

def is_valid_hashtag(hashtag_str):
    pattern = r'\#[a-zA-Z0-9_]+'
    return re.match(pattern, hashtag_str) is not None

# Example Usage
hashtag_1 = "#example"
hashtag_2 = "#ThisIsAHashtag"
hashtag_3 = "invalid-hashtag"

print(f"{hashtag_1} is valid hashtag: {is_valid_hashtag(hashtag_1)}")
print(f"{hashtag_2} is valid hashtag: {is_valid_hashtag(hashtag_2)}")
print(f"{hashtag_3} is valid hashtag: {is_valid_hashtag(hashtag_3)}")

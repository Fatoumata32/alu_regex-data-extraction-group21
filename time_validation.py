import re

def is_valid_time(time_str):
    pattern = r'^(0?[1-9]|1[0-2]):([0-5][0-9]) ?([APap][mM])?$|^([01]?[0-9]|2[0-3]):([0-5][0-9])$'
    return re.match(pattern, time_str) is not None

user_input = input("Enter the time (12-hour or 24-hour) to validate: ")

if is_valid_time(user_input):
    print(f"{user_input} is a valid time.")
else:
    print(f"{user_input} is an invalid time.")

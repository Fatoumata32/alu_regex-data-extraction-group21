# alu_regex-data-extraction-group21
Regex Hackaton

# Data Validation using Regular Expressions

This project consists of a collection of Python scripts designed to validate different types of data using Regular Expressions (regex). Each script is responsible for validating a specific data type such as email addresses, URLs, phone numbers, credit card numbers, time formats, HTML tags, hashtags, and currency amounts.

## Project Structure

The project contains the following Python files:

- `email_validator.py`: Validates email addresses.
- `url_validator.py`: Validates URLs (with or without HTTP/HTTPS).
- `phone_validator.py`: Validates phone numbers in various formats.
- `credit_card_validator.py`: Validates credit card numbers (with spaces or hyphens).
- `time_validator.py`: Validates time in both 12-hour and 24-hour formats.
- `html_tag_validator.py`: Validates basic HTML tags.
- `hashtag_validator.py`: Validates hashtags.
- `currency_validator.py`: Validates currency amounts (with commas and decimal points).

Each script is self-contained and can be executed individually.

## Usage

Each script takes user input and checks whether it matches the required pattern for that particular data type. To use any of the scripts, follow these steps:

1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the Python files.
3. Run any of the Python scripts in your terminal using the following command:
   
   bash
   python <filename>.py

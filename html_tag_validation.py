import re

def is_valid_html_tag(html_str):
    pattern = r'<[^>]+>'
    return re.match(pattern, html_str) is not None

# Example Usage
html_1 = "<p>"
html_2 = "<div class='example'>"
html_3 = "invalid-html"

print(f"{html_1} is valid HTML tag: {is_valid_html_tag(html_1)}")
print(f"{html_2} is valid HTML tag: {is_valid_html_tag(html_2)}")
print(f"{html_3} is valid HTML tag: {is_valid_html_tag(html_3)}")

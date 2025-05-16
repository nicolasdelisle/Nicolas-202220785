import re

text = "Please contact us at support@example.com or sales@company.org. You can also reach out to admin123@school.edu."

# Simple regex that matches any text with '@'  \S+ needed both side for full email adress
email_add = r'\S+@\S+'

email = re.findall(email_add, text)
print(email)
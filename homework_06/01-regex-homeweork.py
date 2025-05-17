import re

text = "Please contact us at support@example.com or sales@company.org. You can also reach out to admin123@school.edu."

# regex that matches any text with '@'  \S+ needed both side for all character until a space each side 
email_add = r'\S+@\S+'

email = re.findall(email_add, text)
print(email)
import re

# Input text
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

# Updated regex pattern to exclude emails from 'exclude.com'
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com\b)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

# Print extracted emails
print(emails)

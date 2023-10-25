# List of email addresses with line breaks
emails = """
"""

# Split the text into individual email addresses and remove empty lines
emails = [email.strip() for email in emails.split('\n') if email.strip()]

# Format the emails as 'email', 'email', ...
formatted_emails = ",\n".join(["    '{}'".format(email) for email in emails])

# Print the formatted emails
print(formatted_emails)

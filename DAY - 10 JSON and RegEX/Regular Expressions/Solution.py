import re

data = [
    "Contact us at support@example.com",
    "Send mail to info@my-site.org or sales@my-site.org",
    "This is not an email: test@.com",
    "admin@company123.net is the admin email",
    "Reach us at user.name@sub.domain.co.in for support"
]

regex = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[com|org|net|co\.in]?"

for Email in data:
    Valid_Email = re.findall(regex, Email)
    if Valid_Email:
        print(Valid_Email)



import re

email = input("Whats your email?").strip()

if re.search(r"^[^@]+@[^@]+\.edu$" , email):
    print("Valid")

else:
    print("Invalid")

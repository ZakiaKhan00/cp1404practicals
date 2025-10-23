"""
CP1404/CP5632 Practical
Emails

Estimate: 30 minutes
Actual:   34 minutes

"""

def main():
    """Store users emails and names in a dictionary"""
    email_to_name = {}
    email = input("Email: ").strip().lower() #cleans whitespace and standardises case
    while email != "" :
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y", "yes"):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    """Extract name from the email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name

main()
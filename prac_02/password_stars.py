"""Program that asks user for a password, verify its length and print asterisks """

MINIMUM_LENGTH = 8

def main():
    """Get valid password and print asterisks"""
    password = get_password()
    print_asterisks(password)

def get_password():
    """Get password of minimum length required."""
    password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    return password

def print_asterisks(password):
    """Print asterisks for the length of the password."""
    print('*' * len(password))

main()
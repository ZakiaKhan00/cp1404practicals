"""On paper, write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word."""

MINIMUM_LENGTH = 4

def main():
    """.Get valid password and print stars"""
    password = get_password(MINIMUM_LENGTH)
    print_stars(password)

def get_password(min_length):
    """Get password from user of minimum length."""
    password = input(f" Enter password of at least {min_length} characters: ")
    while len(password) < min_length:
        print(f"Password too short!")
        password = input(f" Enter password of at least {min_length} characters: ")
    return password

def print_stars(password):
    """Print stars matching the length of the password. """
    print('*' * len(password))

main()
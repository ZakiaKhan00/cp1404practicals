"""Program that asks user for a password, verify its length and print asterisks """

MINIMUM_LENGTH = 8

password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
while len(password) < MINIMUM_LENGTH:
    password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")

print('*' * len(password))
import random
import string

def generate_password():
    length = int(input("Enter password length: "))

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)


def check_password_strength():
    password = input("Enter password to check: ")

    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    if length >= 8 and has_upper and has_lower and has_digit and has_symbol:
        print("Password Strength: STRONG")
    elif length >= 6 and (has_upper or has_lower) and has_digit:
        print(" Password Strength: MEDIUM")
    else:
        print(" Password Strength: WEAK")


while True:
    print("\n Password Tool")
    print("1. Generate Password")
    print("2. Check Password Strength")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        generate_password()
    elif choice == "2":
        check_password_strength()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print(" Invalid choice")
"""
Secure Password Generator

Description:
Generates a secure random password using Python's built-in
secrets module. The user specifies the desired password length,
and the script creates a password using uppercase letters,
lowercase letters, numbers, and special characters.

Author: Nixon Bone
Version: 1.0
"""

import secrets
import string


def generate_password(length):
    """Generate a secure random password."""

    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = "".join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password


def main():
    print("=" * 40)
    print(" Secure Password Generator")
    print("=" * 40)

    try:
        length = int(input("Enter password length: "))

        if length < 8:
            print("\nPassword length should be at least 8 characters.")
            return

        password = generate_password(length)

        print("\nGenerated Password")
        print("-" * 40)
        print(password)

    except ValueError:
        print("\nError: Please enter a valid number.")


if __name__ == "__main__":
    main()

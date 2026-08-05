import secrets
import string

print("=== Secure Password Generator ===")

length = int(input("Enter password length: "))

characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = ''.join(
    secrets.choice(characters)
    for _ in range(length)
)

print("\nGenerated Password:")
print(password)

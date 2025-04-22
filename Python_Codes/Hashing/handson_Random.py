import random
import string

def generate_random_password(length=8):

    # characters = string.ascii_letters + string.digits + string.punctuation
    characters = "AEIOUabcd1234!@#$%^&"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate and print a random password
password = generate_random_password()
print(f"\nRandom password: {password}")

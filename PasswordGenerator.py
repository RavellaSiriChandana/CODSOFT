import random
import string

length = int(input("Enter password length: "))

# All possible characters (letters + digits + symbols)
characters = string.ascii_letters + string.digits + string.punctuation

# Randomly choose characters for the password
password = ''.join(random.choice(characters) for _ in range(length))

print("Your Password is:", password)
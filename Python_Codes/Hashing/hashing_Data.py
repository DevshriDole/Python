import hashlib

# Create a SHA-256 hash object
hash_object = hashlib.sha256()

# Data to be hashed (must be bytes)
data=input("Enter the password")
data=b'data'

# Update the hash object with the data
hash_object.update(data)

# Get the hash value in hexadecimal format
hex_digest_value = hash_object.hexdigest()

# Print the hash
print(hex_digest_value)

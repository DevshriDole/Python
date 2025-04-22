import hashlib

def hash_file(filename):
    """Calculates the SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    with open(filename, 'rb') as file:
        while True:
            chunk = file.read(4096)  # Read in 4KB chunks
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()

# Example usage
file_hash = hash_file("my_file.txt")
print(f"The SHA-256 hash of my_file.txt is: {file_hash}")
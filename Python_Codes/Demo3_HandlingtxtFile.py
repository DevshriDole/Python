
# Function to read data from a text file
def read_from_file(filename):
    try:
        with open(filename, 'r') as file:  # 'r' mode opens the file for reading
            content = file.read()
        print(f"Contents of {filename}:\n{content}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Example usage
filename = 'FileHandling_Example.txt'

# Reading from the file
read_from_file(filename)

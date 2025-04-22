ascii_dict = {}

for char in range(ord('a'), ord('f')):
    ascii_dict[chr(char)] = char

print("\nDictionary of letters and their ASCII values: ")
print(ascii_dict)
    
input_str = input("Enter a string:")
processed_str = input_str.replace(" ","").lower()

char_frequency = {}
for char in processed_str:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print("\nCharacter frequencies: ")
for char, freq in char_frequency.items():
    print(f" '{char}':{freq}")

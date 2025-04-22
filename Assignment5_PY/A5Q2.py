import re

file_path = "D:\\demo.txt"

vowels_counts = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
with open(file_path, 'r') as file:
    content = file.read().lower()
for char in content:
    if char in vowels_counts:
        vowels_counts[char] += 1
print("\nVowel occurrences: ")

for vowel, count in vowels_counts.items():
    print(f"{vowel}:{count}")
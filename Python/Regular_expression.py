import re

text = "I have an apple"
pattern = r'apple'

print(text)
print(pattern)
print("\n***With search()***")
match = re.search(pattern, text)
if match:
    print(f"\nMatch found with search(): '{match.group()}'")
else:
    print("\nMatch not found...")
print("\n---------------")


print("\n***With match()***")
match = re.match(pattern, text)
if match:
     print(f"\nMatch found at the beginning with match(): '{match.group()}'")
else:
     print("\nMatch not found...")
print("\n---------------")


print("\n***With findall()***")
text = "red blue red green red"
pattern = r'red'

matches = re.findall(pattern, text)
print(f"\nMatches found with findall(): {matches}")
print("\n---------------")


print("\n***With sub()***")
text = "Replace all apples with oranges"
pattern = r'apples'
replacement = "oranges"

replaced_text = re.sub(pattern, replacement, text)
print(f"Replaced text with sub(): '{replaced_text}'")
print("\n---------------")


print("\n***With split()***")
text = "apple, banana, orange"
pattern = r','

repalced_text = re.split(pattern, text)
print(f"Replaced text with split(): '{repalced_text}'")
print("\n---------------")

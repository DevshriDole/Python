import re

# text = "Change all instances of cat to dog.."
# pattern = r'cat'
# replacement ="dog"

# replaced_text = re.sub(pattern, replacement, text)
# print(f"Replaced text with sub(): '{replaced_text}'")
# print("\n---------------")

text = "hello hello hello hello"
pattern = r'hello'

matches = re.findall(pattern, text)
print(f"\nMatches found with findall(): {matches}")
print("\n---------------")
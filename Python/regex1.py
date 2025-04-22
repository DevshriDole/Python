import re
# text = "banana is my favorite fruit."
# pattern = r'banana'

# print(text)
# print(pattern)
# print("\n***With search()***")
# match = re.search(pattern, text)
# if match:
#     print(f"\nMatch found with search(): '{match.group()}'")
# else:
#     print("\nMatch not found...")
# print("\n---------------")


# print("\n***With match()***")
# match = re.match(pattern, text)
# if match:
#      print(f"\nMatch found at the beginning with match(): '{match.group()}'")
# else:
#      print("\nMatch not found...")
# print("\n---------------")

# text = "I have an apple,but i want orange"
# pattern = r'orange'

# print(text)
# print(pattern)
# print("\n***With search()***")
# match = re.search(pattern, text)
# if match:
#     print(f"Match found with search(): '{match.group()}'")
# else:
#     print("Match not found...")
# print("\n---------------")


# print("\n***With match()***")
# match = re.match(pattern, text)
# if match:
#      print(f"Match found at the beginning with match(): '{match.group()}'")
# else:
#      print("Match not found...")
# print("\n---------------")

text = "The quick brown fox."
pattern = r'quick'

print(text)
print(pattern)
print("\n***With search()***")
match = re.search(pattern, text)
if match:
    print(f"Match found with search(): '{match.group()}'")
else:
    print("Match not found...")
print("---------------")


print("\n***With match()***")
match = re.match(pattern, text)
if match:
     print(f"Match found at the beginning with match(): '{match.group()}'")
else:
     print("Match not found...")
print("---------------")
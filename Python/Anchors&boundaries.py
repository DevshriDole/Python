import re

text = "Start. This is the starting point of the paragraph..."
text1 = "To end the paragraph, we simply put End"

pattern = r'^Start'
match = re.search(pattern, text)
print("\nMatch found...", match.group())

pattern = r'End$'
match = re.search(pattern, text1)
print("\nMatch found...", match.group())

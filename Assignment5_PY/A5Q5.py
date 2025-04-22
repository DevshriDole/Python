import re

text = """Here are some details: Aadhar: 7219 8765 4567, PAN: ABCDE1234A, 
Another Aadhar: 1234 5678 9012, Fake one: 12345 678 901
"""
aadhar_pattern = r'\b\d{4} \d{4} \d{4}\b'
aadhar_numbers = re.findall(aadhar_pattern, text)
print(aadhar_numbers)
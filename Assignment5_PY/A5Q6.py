import re

text = """
Aadhar: 7219 8765 4567, PAN1: BUYKU6767J, PAN2: ABcde1234F, Invalid: 1234567890, PAN3: PLMNB1234K
"""
pan_pattern = r'\b[A-Z]{5}[0-9]{4}[A-Z]\b'

pan_numbers = re.findall(pan_pattern, text)

print(pan_numbers)
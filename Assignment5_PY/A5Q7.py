import re 

text = """
 DOB is: 12\\05\\1997. Another one: 31\\12\\2000.
Invalid one: 32\\30\\2020, 5/06/1995, 01-01-2001
"""
date_pattern = r'\b(?:0[1-9]|[12][0-9]|3[0-1])\\(?:0[1-9]|1[0-2])\\(?:19|20)\d{2}\b'
birth_dates = re.findall(date_pattern, text)
# dobs = ['\\'.join(match) for match in birth_dates]

print("Extracted Dates of Birth:")
print(birth_dates)





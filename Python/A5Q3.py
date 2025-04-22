
import re

demo = "D:\\test.txt"
with open(demo, 'r') as file:
    for line in file:
        pattern = r'^[Quick].+[Horse]$'
        
        if re.match(pattern, line):
            print(f"Match found: {line.strip()}")
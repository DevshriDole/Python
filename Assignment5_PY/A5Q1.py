import re

file_path = "D:\\demo.txt"
with open(file_path, 'r') as file:
    content = file.read()
    pattern = r'after'
    replacement = "before"

modified_content = re.sub(pattern, replacement,content)    

with open(file_path,'w') as file:
    file.write(modified_content)

print("Keyword 'after' replaced with 'before'.\n ",modified_content)    



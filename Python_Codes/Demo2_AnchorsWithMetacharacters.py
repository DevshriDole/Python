import re

text = "Start when there is still time so that we are good at the end"
# pattern = r'^Start'
# pattern = r'end$'

pattern = r'^Start.+end$' # Works
# pattern = r'^Start.*end$' # Works
# pattern = r'^Start.?end$' # Fails

strMatchedVal = re.search(pattern,text)
print (strMatchedVal.group())

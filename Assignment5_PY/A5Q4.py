import re
text="I wish to join:Google123,apple,Meta##,Amazon,X,Microsoft...,Tesla,NASA(),ISRO"
text1=text.strip(':').split(',')
pattern=r'^[A-Za-z].+[A-Za-z]$'
for i in text1:
    if i in text1:
        match=re.findall(pattern,i)
        if match:  
            print(i)
    
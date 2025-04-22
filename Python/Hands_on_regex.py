import re
text = "Dog, Fox, Horse, Lion, Tiger, zebra, cat "

pattern = r'Dog|cat|zebra|Horse'

# lstAnimalnames = text.split(",")
# lstFinalnames = []

# for animal in lstAnimalnames:
match = re.findall(pattern, text)
    
    # if match:
        # lstFinalnames.append(animal)
print(match)
        





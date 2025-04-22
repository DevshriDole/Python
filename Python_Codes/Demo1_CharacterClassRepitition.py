
import re

pattern = "^[A-Z]\w[0-9][0-9][0-9]$" # - o/p : ['PQ123', 'AB567']
# pattern = "^[A-Z]\w*[0-9]{2}$" # o/p : ['PQ123', 'AB567']
# pattern = "[A-Z]{2}(-+)[0-9]{2}"  o/p : ['CIP--876', 'AYK--579']
# pattern = "CIP--876|AYK--579" o/p : ['CIP--876', 'AYK--579']

text = "Here is a list of product codes:PQ123,AN-RFT,AB567,CIP--876,AYK--579"

lst_productNames = text.split(":")[1].split(",")

print(lst_productNames)
lstvalidNames = []
for name in lst_productNames:
    str_Matched_Value = re.search(pattern,name)
    if str_Matched_Value:
        lstvalidNames.append(name)

print(lstvalidNames)

#
# pattern = "[0-9][0-9][0-9]$"
# lstvalidNames_final = []
# for name in lstvalidNames:
#     match = re.search(pattern,name)
#     print(match)
#     if match:
#         lstvalidNames_final.append(name)
#
# print(lstvalidNames_final)

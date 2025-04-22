str = input("\nEnter elements of a tuple seperated by commas:")
elements = tuple(eval(x.strip()) for x in str.split(','))

element_to_repeat = eval(input("\nEnter the element you want to repeat:"))
repeat_count = int(input("\nEnter how many times to repeated:"))

new_tuple = tuple()
for item in elements:
    if item == element_to_repeat:
        new_tuple += (item, ) * repeat_count
    else:
        new_tuple += (item, )

print("\nOriginal tuple: ", elements)
print("\nNew tuple: ", new_tuple) 
                       
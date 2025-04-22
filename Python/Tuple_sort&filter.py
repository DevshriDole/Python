my_tuple = input("\nEnter the values in tuple seperated by commas: ")

tuple_sort = tuple(int(x.strip()) for x in my_tuple.split(','))
print("\nOriginal tuple is: ", tuple_sort)

asce_tuple = tuple(sorted(tuple_sort))

threshold = int(input("Enter a value to filter elements greater than it:"))
filter_element = tuple(x for x in asce_tuple if x > threshold)

print("\nTuple in ascending order is: ", asce_tuple)
print("\nFiltered elements are: ", filter_element)


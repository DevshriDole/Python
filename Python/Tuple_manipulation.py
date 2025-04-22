my_tuple = input("\nEnter elements in a tuple seperated by commas: ")
int_tuple = tuple(int(x.strip()) for x in my_tuple.split(','))

first_element = int_tuple[0]
last_element = int_tuple[-1]
slice_tuple = int_tuple[1:-1]
every_second = int_tuple[::2]
reversed_tuple = int_tuple[::-1]


print("\nOriginal tuple is: ", int_tuple)
print("\nFirst element of the tuple is: ", first_element)
print("\nLast element of the tuple is: ", last_element)
print("\nTuple after excluding first and last element is: ", slice_tuple)
print("\nEvery second elemnt of a tuple is: ", every_second)
print("\nReversed tuple is: ", reversed_tuple)


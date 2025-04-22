my_tuple = input("\nEnter the values in tuple seperated by commas: ")
int_tuple = tuple(int(x.strip()) for x in my_tuple.split(','))

total = sum(int_tuple)
average = total / len(int_tuple)
maximum = max(int_tuple)
minimum = min(int_tuple)
count = len(int_tuple)

print("\nTuple is: ", int_tuple)
print("\nSum of all elements in a tuple is: ", total)
print("\nAverage of the elements is: ", average)
print("\nMaximum value in tuple is: ", maximum)
print(f"\nMinimum value in a tuple is: {minimum}")
print(f"\nNumber of elements in a tuple is: {count}")







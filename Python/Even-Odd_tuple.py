new_tuple = (1,2,3,6,9,10)
even_tuple = ()
odd_tuple = ()

for i in  new_tuple:
    if i % 2 == 0:
        even_tuple += (i,)
    else:
        odd_tuple += (i,)
print("\nEven tuple is: ", even_tuple)
print("\nOdd tuple is: ", odd_tuple)
str = input("Enter a string:")
print(str)

processed_str = str.replace(" ","").lower()
if processed_str == processed_str[::-1]:
    print("\nThe string is a palindrome.")
else:
    print("\nString is not a palindrome.")



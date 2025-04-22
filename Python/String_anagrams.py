str1 = input("Enter the first string:")
str2 = input("Enter second string:")

str1_processed = str1.replace(" ","").lower()
str2_processed = str2.replace(" ","").lower()

if sorted(str1_processed) == sorted(str2_processed):
    print("\nThe strings are anagrams.")
else:
    print("\nThe strings are not anagrams.")

    
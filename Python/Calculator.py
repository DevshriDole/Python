# x = 10
# y = 5
# print("----------")

x = int(input("Enter 1st no : "))
y = int(input("Enter 2nd no :"))

operator = input("\nEnter any operator:")

if operator == '+':
    result = x + y
    print("\nResult=", result)
elif operator == '-':
    result = x - y
    print("\nResult=", result)
elif operator == '*':
    result = x * y
    print("\nResult=", result)
elif operator == '/':
    result = x / y
    print("\nResult=", result)
else:
    print("\nInvalid operator...")

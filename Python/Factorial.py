n = int(input("\nEnter a number:"))
factorial = 1

# for i in range(1, n + 1):
#     factorial *= i
# print("\nFactorial of a number is:", factorial)



i = 1
while i <= n:
    factorial *= i
    i += 1
print("\nFactorial of a number is:", factorial)


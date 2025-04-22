num = int(input("\nEnter a number:"))

sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print("\nSum of digits of a number is:", sum)

a = 1
b = 2
fibonacci_series = []

while b <= 100:
    if b >= 2:
        fibonacci_series.append(b)
    a , b = b, a + b
print("\n Fibonacci series from 2 to 100 is: ")
print(fibonacci_series)


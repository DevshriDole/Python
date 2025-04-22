def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
         if num % i == 0:
            return False
    return True 
try:
   n = int(input("Enter a positive integer:")) 
   if n <= 0:
      print("Please enter a positive integer greater then zero.")   
   else:
      prime_list = []
      for number in range(2,n+1):
         if is_prime(number):
            prime_list.append(number)
         print(f"prime numbers upto to {n}: {prime_list}")
except ValueError:
   print("Invalid input .Please enter a valid integer.")             
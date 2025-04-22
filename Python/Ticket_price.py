age = int(input("Enter your age:"))

if age < 5:
    price = 0
    print("\nTicket is free...")
else:
    if age <= 12:
        price = 5
        print("\nYour ticket price is Rs",price)
    else:
        if age <= 60:
            
            price = 10
            print("\nYour ticket price is Rs",price)
        else:
            price = 7
            print("\nYour ticket price is Rs",price)


inventory = {}
def add_item():
    item = input("\nEnter item name:")
    if item in inventory:
        print("Item already exists. Use update options to modify.")
        return
    quantity = int(input("\nEnter quantity:"))
    price = float(input("\nEnter price per item:"))
    inventory [ item] = {"quantity": quantity, "price": price}
    print(f"{item} added successfully.")

def update_item():
    item = input("\nEnter item name to update:")
    # if item not in inventory:
        # print("\nItem not found in inventory.")
        # return
    choice = input("\nWhat would you like to update? Quantity/Price/Both: ").lower() 
    if choice == "quantity":
        quantity = int(input("\nEnter new quantity: "))
        inventory[item]["quantity"] = quantity
    elif choice == "price":
        price = float(input("\nEnter new price: ")) 
        inventory[item]["price"] = price
    elif choice == "both":
        quantity =int(input("\nEnter new quantity: "))
        price = float(input("\nEnter new price: "))
        inventory[item]["quantity"] = quantity
        inventory[item]["price"] = price
    else:
        print("\nInvalid option.")
        return
    print(f"{item} updated successfully.") 

def display_inventory():
    if not inventory:
        print("\nInventory is empty.")
        return
    print("\nCurrent inventory")
    print("{:<15} {:<10} {:<10}".format("Item", "Quantity", "Price"))
    for item, details in inventory.items():
        print("{:<15} {:<10} {:<10.2f}".format(item, details["quantity"], details["price"]))

def calculate_total_value():
    total = 0
    for details in inventory.values():
        total += details["quantity"] * details["price"] 
    print(f"\nTotal inventory value: Rs. {total:.2f}")

def menu():
    while True:
        print("\nInventory management menu: ")
        print("\n1.Add item")
        print("\n2.Update item")
        print("\n3.Display inventory")  
        print("\n4.Calculate total number ")
        print("\n5.Exit") 
        choice = input("\nEnter your choice (1-5): ") 
        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            display_inventory()
        elif choice == "4":
            calculate_total_value()
        elif choice == "5":
            print("\nExisting inventory management system.")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")

menu()

  
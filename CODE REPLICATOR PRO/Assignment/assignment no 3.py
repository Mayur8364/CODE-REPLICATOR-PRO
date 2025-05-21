# Inventory Management System
# Name: Ganesh Wagh
# Roll No: 133
# Batch: AIDS-B3

inventory = {}

while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Display Inventory")
    print("3. Remove Item")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        item_name = input("Enter item name: ")
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        if item_name in inventory:
            inventory[item_name] += quantity
        else:
            inventory[item_name] = quantity
        print(f"{item_name} added/updated with quantity {quantity}")

    elif choice == 2:
        if inventory:
            print("\nCurrent Inventory:")
            for item, quantity in inventory.items():
                print(f"{item}: {quantity}")
        else:
            print("Inventory is empty.")

    elif choice == 3:
        item_name = input("Enter item name to remove: ")
        try:
            quantity_to_remove = int(input("Enter quantity to remove: "))
            if quantity_to_remove < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            continue

        if item_name in inventory:
            if inventory[item_name] > quantity_to_remove:
                inventory[item_name] -= quantity_to_remove
                print(f"{quantity_to_remove} of {item_name} removed from inventory.")
            elif inventory[item_name] == quantity_to_remove:
                del inventory[item_name]
                print(f"{item_name} has been removed from inventory.")
            else:
                print(f"Not enough quantity of {item_name} to remove. Only {inventory[item_name]} left.")
        else:
            print(f"{item_name} not found in the inventory.")

    elif choice == 4:
        print("Exiting the inventory system.")
        break

    else:
        print("Invalid choice. Please try again.")


'''Output:

(base) aids@aids-OptiPlex-3000:~$ python3 Ganesh Wagh5.py
Inventory Management System
1. Add Item
2. Display Inventory
3. Remove Item
4. Exit
Enter your choice: 1
Enter item name: Dell
Enter quantity: 50
Dell added/updated with quantity 50

Inventory Management System
1. Add Item
2. Display Inventory
3. Remove Item
4. Exit
Enter your choice: 1
Enter item name: Dell
Enter quantity: 70
Dell added/updated with quantity 70

Inventory Management System
1. Add Item
2. Display Inventory
3. Remove Item
4. Exit
Enter your choice: 1
Enter item name: Lenovo
Enter quantity: 100
Lenovo added/updated with quantity 100

Inventory Management System
1. Add Item
2. Display Inventory
3. Remove Item
4. Exit
Enter your choice: 2

Current Inventory:
Dell: 120
Lenovo: 100

Inventory Management System
1. Add Item
2. Display Inventory
3. Remove Item
4. Exit
Enter your choice: 3
Enter item name to remove: Lenovo
Enter quantity to remove: 50
50 of Lenovo removed from inventory.

Inventory Management System
1. Add Item
2. Display Inventory
3. Remove Item
4. Exit
Enter your choice: 4
Exiting the inventory system.'''

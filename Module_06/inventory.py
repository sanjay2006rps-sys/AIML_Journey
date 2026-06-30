inventory = {"Laptop": 85000, "Mouse": 600, "Keyboard": 1500}
while True:
    choice = input("1.Add 2.Update 3.Delete 4.Search 5.Show 6.Exit: ")
    if choice == "1":
        name, price = input("Name: "), float(input("Price: "))
        inventory[name] = price
    elif choice == "2":
        name = input("Product: ")
        if name in inventory:
            inventory[name] = float(input("New price: "))
    elif choice == "3":
        inventory.pop(input("Product: "), None)
    elif choice == "4":
        print(inventory.get(input("Product: "), "Not found"))
    elif choice == "5":
        for p, c in inventory.items(): print(f"{p}: ₹{c}")
    elif choice == "6":
        break
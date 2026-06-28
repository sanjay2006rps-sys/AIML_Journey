cart = []

while True:
    print("\n1.Add  2.Remove  3.Show Cart  4.Exit")
    choice = input("Choose: ")

    if choice == "1":
        item = input("Item name: ")
        cart.append(item)
        print(f"'{item}' added.")
    elif choice == "2":
        item = input("Item to remove: ")
        if item in cart:
            cart.remove(item)
            print(f"'{item}' removed.")
        else:
            print("Item not in cart.")
    elif choice == "3":
        print("Cart:", cart, f"({len(cart)} items)")
    elif choice == "4":
        print("Goodbye!")
        break

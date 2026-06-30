balance = 0
def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ₹{amount}. New balance: ₹{balance}")
def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print(f"Withdrew ₹{amount}. New balance: ₹{balance}")
def check_balance():
    print(f"Current balance: ₹{balance}")
def show_menu():
    while True:
        choice = input("1.Deposit 2.Withdraw 3.Balance 4.Exit: ")
        if   choice == "1":
            deposit(float(input("Amount: ")))
        elif choice == "2":
            withdraw(float(input("Amount: ")))
        elif choice == "3":
            check_balance()
        elif choice == "4":
            break
show_menu() 
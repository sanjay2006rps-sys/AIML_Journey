def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)

def reverse_string(s):
    if len(s) == 0:
        return ""
    return reverse_string(s[1:]) + s[0]

def menu():
    print("\n1. Factorial")
    print("2. Fibonacci")
    print("3. Sum of Numbers")
    print("4. Reverse String")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        n = int(input("Enter a number: "))
        print("Factorial =", factorial(n))
        menu()
    elif choice == "2":
        n = int(input("Enter a number: "))
        print("Fibonacci =", fibonacci(n))
        menu()
    elif choice == "3":
        n = int(input("Enter a number: "))
        print("Sum =", sum_numbers(n))
        menu()
    elif choice == "4":
        s = input("Enter a string: ")
        print("Reversed =", reverse_string(s))
        menu()
    elif choice == "5":
        print("Exiting...")
    else:
        print("Invalid choice")
        menu()

menu()
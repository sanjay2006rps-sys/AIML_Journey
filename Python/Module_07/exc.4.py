def odd_even(n):
    return "Even" if n%2==0 else "Odd"
value=int(input("Enter the value:"))
find=odd_even(value)
print(f"The given number is {find}")
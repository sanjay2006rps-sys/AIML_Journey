numbers = [10, 20, 30]       # list
print("Original list :", numbers, type(numbers))

converted = tuple(numbers)   # → tuple
print("As tuple      :", converted, type(converted))

back = list(converted)        # → list again
print("Back to list  :", back, type(back))
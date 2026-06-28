names = ["Sanjay", "Rahul", "Sanjay", "Amit", "Rahul", "Priya"]
print("Original list :", names)
print("With duplicates:", len(names))

unique = list(set(names))
print("Unique names  :", unique)
print("Count         :", len(unique))
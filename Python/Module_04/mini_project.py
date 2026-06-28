record = ("Sanjay", 19, "Computer Science", 8.7)
name, age, dept, cgpa = record

print(f"Name      : {name}")
print(f"Age       : {age}")
print(f"Department: {dept}")
print(f"CGPA      : {cgpa}")

# Update CGPA — tuple → list → tuple
new_cgpa = float(input("Enter new CGPA: "))
temp = list(record)
temp[3] = new_cgpa
record = tuple(temp)
print("Updated record:", record)
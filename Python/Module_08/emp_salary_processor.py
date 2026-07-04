employees = [
    ("Sanjay", 35000),
    ("Rahul", 50000),
    ("Amit", 42000),
    ("Priya", 60000)
]

# Sort by salary (highest first)
sorted_employees = sorted(employees, key=lambda x: x[1], reverse=True)
print(sorted_employees)

# Display employees earning more than 40,000
high_earners = list(filter(lambda x: x[1] > 40000, employees))
print(high_earners)

# Increase every salary by 10%
updated_salaries = list(map(lambda x: (x[0], int(x[1] * 1.10)), employees))
print(updated_salaries)
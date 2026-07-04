students = [
    {"name": "Sanjay", "marks": 88},
    {"name": "Rahul", "marks": 95},
    {"name": "Amit", "marks": 76},
    {"name": "Priya", "marks": 91}
]

# Sort by marks
sorted_students = sorted(students, key=lambda x: x["marks"])
print(sorted_students)

# Filter students with marks >= 90
top_students = list(filter(lambda x: x["marks"] >= 90, students))
print(top_students)

# Add 5 bonus marks to every student, maximum 100
bonus_students = list(map(lambda x: {"name": x["name"], "marks": min(x["marks"] + 5, 100)}, students))
print(bonus_students)
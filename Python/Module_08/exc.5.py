students = [
    ("Sanjay", 19),
    ("Rahul", 21),
    ("Amit", 18)
]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
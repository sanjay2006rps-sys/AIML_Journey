student = {"id": 101, "name": "Sanjay", "age": 19, "cgpa": 8.7, "skills": []}
while True:
    choice = input("1.Show 2.Update CGPA 3.Add Skill 4.Exit: ")
    if choice == "1":
        for k, v in student.items(): print(f"{k}: {v}")
    elif choice == "2":
        student["cgpa"] = float(input("New CGPA: "))
    elif choice == "3":
        student["skills"].append(input("Skill: "))
    elif choice == "4":
        break
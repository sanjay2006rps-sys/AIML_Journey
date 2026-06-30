marks = {"Math": 90, "Physics": 85, "Python": 95}
subject = input("Enter subject: ")
result = marks.get(subject, "Subject Not Found")
print(result)
def get_marks():
    return [int(input(f"Subject {i+1}: ")) for i in range(5)]
def calculate_average(marks):
    return sum(marks) / len(marks)
def calculate_grade(avg):
    if   avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"
def display_result(marks, avg, grade):
    print("Marks  :", marks)
    print(f"Average: {avg:.1f}")
    print(f"Grade  : {grade}")
marks = get_marks()
avg   = calculate_average(marks)
grade = calculate_grade(avg)
display_result(marks, avg, grade)
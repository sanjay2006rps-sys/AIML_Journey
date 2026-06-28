marks = [int(input(f"Subject {i+1} marks: ")) for i in range(5)]

print("Highest:", max(marks))
print("Lowest :", min(marks))
print("Total  :", sum(marks))
avg = sum(marks) / len(marks)
print(f"Average: {avg:.1f}")

if avg >= 90:
    print("Excellent")
elif avg >= 75:
    print("Good")
else:
    print("Needs Improvement")
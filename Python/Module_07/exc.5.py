def marks_stats(marks):
    highest = max(marks)
    lowest  = min(marks)
    average = sum(marks) / len(marks)
    return highest, lowest, average
x,y,z= marks_stats([78, 92, 85, 60, 99])
print("Highest:",x)
print("Lowest :",y)
print("Average:",z)
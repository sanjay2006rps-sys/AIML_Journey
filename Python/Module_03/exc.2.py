numbers = [int(input("Enter number: ")) for _ in range(5)]

print("Largest :", max(numbers))
print("Smallest:", min(numbers))
print("Sum     :", sum(numbers))
print("Average :", sum(numbers) / len(numbers))
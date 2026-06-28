nums = set()
for i in range(10):
    n = int(input(f"Number {i+1}: "))
    nums.add(n)

print("Unique numbers:", nums)
print("Count         :", len(nums))
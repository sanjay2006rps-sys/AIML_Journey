fruits = {"apple", "mango", "banana", "grape", "kiwi"}

fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
    print(f"✅ '{fruit}' found in the set!")
else:
    print(f"❌ '{fruit}' not found.")
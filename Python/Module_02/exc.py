# ============================================================
# STRING EXERCISES - Python Practice
# ============================================================

# ----------------------------
# Exercise 1: Full Name Cases
# ----------------------------
print("=" * 40)
print("       EXERCISE 1 - Name Cases")
print("=" * 40)

name = input("Enter your full name: ")

print(f"Upper : {name.upper()}")
print(f"Lower : {name.lower()}")
print(f"Title : {name.title()}")
print(f"Length: {len(name)}")


# ----------------------------
# Exercise 2: String Slicing
# ----------------------------
print("\n" + "=" * 40)
print("     EXERCISE 2 - String Slicing")
print("=" * 40)

sentence = input("Enter a sentence: ")

print(f"First character    : {sentence[0]}")
print(f"Last character     : {sentence[-1]}")
print(f"First 5 characters : {sentence[:5]}")
print(f"Last 5 characters  : {sentence[-5:]}")


# ----------------------------
# Exercise 3: Word & Char Count
# ----------------------------
print("\n" + "=" * 40)
print("   EXERCISE 3 - Word & Char Count")
print("=" * 40)

sentence = input("Enter a sentence: ")

word_count = len(sentence.split())
char_count = len(sentence)

print(f"Number of words      : {word_count}")
print(f"Number of characters : {char_count}")


# ----------------------------
# Exercise 4: Email Validator
# ----------------------------
print("\n" + "=" * 40)
print("     EXERCISE 4 - Email Validator")
print("=" * 40)

email = input("Enter your email: ")

if "@" in email:
    print("Valid Email ✅")
else:
    print("Invalid Email ❌")


# ----------------------------
# Exercise 5: Space Replacer
# ----------------------------
print("\n" + "=" * 40)
print("     EXERCISE 5 - Space Replacer")
print("=" * 40)

sentence = input("Enter a sentence: ")

result = sentence.replace(" ", "_")
print(f"Result: {result}")

print("\n" + "=" * 40)
print("       All Exercises Complete!")
print("=" * 40)
# ============================================================
#         MINI PROJECT + INTERMEDIATE CHALLENGE
# ============================================================


# ============================================================
# MINI PROJECT - Student Email Generator
# ============================================================
print("=" * 45)
print("       Student Email Generator")
print("=" * 45)

first_name = input("Enter First Name : ").strip().lower()
last_name  = input("Enter Last Name  : ").strip().lower()
college    = input("Enter College    : ").strip().lower().replace(" ", "")

last_initial = last_name[0]

email = f"{first_name}.{last_initial}@{college}.edu"

print("\nGenerated Email:")
print(f"  {email}")


# ============================================================
# INTERMEDIATE CHALLENGE - Password Strength Checker
# ============================================================
print("\n" + "=" * 45)
print("       Password Strength Checker")
print("=" * 45)

password = input("Enter a password : ")

has_upper  = any(c.isupper() for c in password)
has_lower  = any(c.islower() for c in password)
has_digit  = any(c.isdigit() for c in password)
has_length = len(password) >= 8

# Detailed feedback
print("\n--- Strength Report ---")
print(f"  Min 8 characters   : {'✅' if has_length else '❌'} ({len(password)} given)")
print(f"  Uppercase letter   : {'✅' if has_upper  else '❌'}")
print(f"  Lowercase letter   : {'✅' if has_lower  else '❌'}")
print(f"  Contains a digit   : {'✅' if has_digit  else '❌'}")

if has_length and has_upper and has_lower and has_digit:
    print("\n  Result → Strong Password 💪")
else:
    print("\n  Result → Weak Password ⚠️")

print("=" * 45)

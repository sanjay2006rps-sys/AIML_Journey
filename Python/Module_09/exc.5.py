def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

word = "madam"
print("Palindrome" if is_palindrome(word) else "Not Palindrome")
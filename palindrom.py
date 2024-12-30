def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
s = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(s):
    print("True - It's a palindrome!")
else:
    print("False - It's not a palindrome.")

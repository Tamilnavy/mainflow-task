
str1 = input("Enter the first string: ").replace(" ", "").lower()
str2 = input("Enter the second string: ").replace(" ", "").lower()

anagram = sorted(str1) == sorted(str2)

print(anagram)

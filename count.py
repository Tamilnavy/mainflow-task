user_string = input("Enter a string: ")
user_string = user_string.lower()
vowel_count = 0
consonant_count = 0
vowels = "aeiou"
for char in user_string:
    if char.isalpha():  
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")

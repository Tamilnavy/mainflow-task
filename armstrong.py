def is_armstrong_number(n):
    digits = str(n)
    num_digits = len(digits)
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    return armstrong_sum == n
n = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong_number(n):
    print("True - It's an Armstrong number!")
else:
    print("False - It's not an Armstrong number.")

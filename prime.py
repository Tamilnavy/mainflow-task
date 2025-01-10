import math

def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n <= 3:
        return True  # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate multiples of 2 and 3

    # Check divisors from 5 to sqrt(n), skipping even numbers
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 2):
        if n % i == 0:
            return False
    return True

# Input from the user
n = int(input("Enter a number to check if it's prime: "))

# Output the result
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

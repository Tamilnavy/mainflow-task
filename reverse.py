def reverse_with_method(my_list):
    my_list.reverse()
    return my_list

def reverse_with_slicing(my_list):
    return my_list[::-1]

def reverse_with_loop(my_list):
    reversed_list = []
    for item in my_list:
        reversed_list.insert(0, item)
    return reversed_list

def reverse_with_recursion(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_with_recursion(lst[:-1])

print("Choose a method to reverse the list:")
print("1. Built-in reverse() method")
print("2. Slicing")
print("3. Loop")
print("4. Recursion")

choice = int(input("Enter your choice (1-4): "))
my_list = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))

if choice == 1:
    result = reverse_with_method(my_list)
elif choice == 2:
    result = reverse_with_slicing(my_list)
elif choice == 3:
    result = reverse_with_loop(my_list)
elif choice == 4:
    result = reverse_with_recursion(my_list)
else:
    print("Invalid choice!")
    exit()

print("Reversed list:", result)

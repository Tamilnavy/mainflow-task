my_list = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))

sorted_list_ascending = sorted(my_list)

sorted_list_descending = sorted(my_list, reverse=True)

print("Original list:", my_list)
print("Sorted list (ascending):", sorted_list_ascending)
print("Sorted list (descending):", sorted_list_descending)

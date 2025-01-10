my_list = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
unique_list = list(set(my_list))
unique_list.sort()
print("List without duplicates:", unique_list)

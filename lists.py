# Lists are mutable, meaning their contents can be modified after creation.
my_list = [1, 2, 3, 4, 5]
#
# # Modifying a list element
my_list[2] = 10
# print(my_list)  # Output: [1, 2, 10, 4, 5]

# # Appending an element
# my_list.append(900)
# print(my_list)  # Output: [1, 2, 10, 4, 5, 6]

# Removing an element
my_list.remove(1)
print(my_list)  # Output: [1, 10, 4, 5, 6]
# Tuples are immutable, meaning their contents cannot be changed after creation.
my_tuple = (1, 2, 3, 4, 5)

# Attempting to modify a tuple element (will result in an error)
# my_tuple[2] = 10  # This will raise a TypeError

# # Concatenating tuples to create a new tuple
# new_tuple = my_tuple + (6, 7)
# print(new_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)

# Slicing and indexing a tuple is allowed
print(my_tuple[3:5])  # Output: 4

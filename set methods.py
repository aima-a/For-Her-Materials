# Creating two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using .add() to add an element to a set
# set1.add(5)
# print(set1)

# Using .remove() to remove a specified element from a set
# set1.remove(2)
# print(set1)

# Using .pop() to remove and return a random element from a set
# print(set1.pop())  # Output: The popped element

# Using .clear() to remove all elements from a set
# set1.clear()
# print(set1)  # Output: set(), {}
#
# Creating two sets again
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using .union() to return the union of two sets 'union = and'
# union_set = set1.union(set2)
# print(union_set)  # Output: {1, 2, 3, 4, 5, 6}
#
# Using .intersection() to return the intersection of two sets
# intersection_set = set1.intersection(set2)
# print(intersection_set)  # Output: {3, 4}

# Using .difference() to return the difference between two sets
# What is present in set 1 that is not present in set 2?
difference_set1 = set1.difference(set2)
print(difference_set1)  # Output: {1, 2}
difference_set2 = set2.difference(set1)
print(difference_set2) # Output: {5, 6}


'''
'''


# This is a comment
# This a comment
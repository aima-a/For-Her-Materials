# Given strings
s1 = "Ault"
s2 = "Kelly"

# Calculate the midpoint index of s1
mid_index = len(s1) // 2

# Split s1 into two parts: before and after the midpoint
s1_before = s1[:mid_index]  # Characters before the midpoint
s1_after = s1[mid_index:]   # Characters after or at the midpoint

# Concatenate s1_before, s2, and s1_after to create s3
s3 = s1_before + s2 + s1_after

# Print the result
print(s3)

'''Explanation:
- mid_index calculates the index at which we want to insert s2. We use integer division // to ensure we get a whole number.
- s1_before contains the characters before the midpoint of s1, and s1_after contains the characters at or after the midpoint.
- We concatenate s1_before, s2, and s1_after to create the final string s3 with s2 inserted in the middle.
- The result is printed, and the output will be AuKellylt as expected.'''
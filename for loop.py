'''this is a docstring'''  # This is a comment

'''Basic for loop'''
fruits = ["apple", "banana", "cherry"]
# print('I love', fruits)
# for fruit in fruits:    # This for loop will execute 3 times
#     print('I love', fruit)

'''For loop with range'''
# for num in range(1, 6):  # This for loop will execute 5 times
#     print(f'My number is {num}')

'''Iterating through a range of numbers and adding them all up together'''
# Initialize a count-er variable to store the sum
total_sum = 0

# Loop from 3 to 199 (inclusive)

for n in range(3, 200):
    if n % 2 == 0: # If the number is even
        total_sum += n # Add the current number to the total_sum

# Print the result
print("The sum of even numbers from 3 to 200 is:", total_sum)

# '''For loop with range and optional step value'''
# for i in range(1,21,2): # From 1-20 skipping every other number
#     print(i)

# '''Break:'''
# for num in [1, 2, 3, 4, 5]:
#     if num == 3:
#         break  # Exit the loop when num is 3
#     print(num)
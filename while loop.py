'''While loop, while loop with break, while loop with continue'''

# # While:
# count = 0
# while count < 5:
#     count += 1
#     print(count)    # While count is <5


# Break:
# for num in [1, 2, 3, 4, 5]:
#     if num == 3:
#         break  # Exit the loop when num is 3
#     print(num)

# Continue:
x = 0
while x < 11:
    x += 1
    if x == 5:
        continue    # Skips the current iteration of the loop when x is 5
    print(x)


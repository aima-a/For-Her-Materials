'''While loop, while loop with continue'''

# While loop:
# count = 0
# while count < 5:    # As long as count is less than 5, this loop will execute (5 times)
#     count += 1      # Adding 1 to count every time this loop executes
#     print(count)    # While count is <5

# Continue:
x = 0
while x < 11:
    x += 1
    if x == 5:
        continue    # Skips the current iteration of the loop when x is 5
    print(x)


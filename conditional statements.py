# y = 2.3
x = float(input('Enter a number: '))  # Convert user input from string to integer
print(x)
if x > 10:      # Initial condition
    print('x is greater than 10')
elif x < 10:    # Additional condition
    print('x is less than 10')
else:
    print('x is equal to 10')   # Default condition


a = 'bob'
b = 'Bob'
if a == b:
    print('Both strings are the same')
else:
    print('Different strings')
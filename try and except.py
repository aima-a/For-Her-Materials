'''This program divides 10 by any number the user inputs'''

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:  # Built-in exception
    print("Cannot divide by zero")
except ValueError:  # Built-in exception
    print("Invalid input. Enter a valid number."
          
'''Note: reformat your code for better readability'''

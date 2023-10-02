'''Defining a function, returning a value, and calling a function'''

def calculate_area(length, width):
    """Calculate the area of a rectangle."""  # Use docstrings to describe your function
    area = length * width  # Variables defined within a function cannot be called outside of that function
    return print(f'The area of the rectangle is {area}')  # This returns the area, otherwise the function would not return anything after running


calculate_area(1, 2)  # You must call your function to run it; include arguments instead of parameters


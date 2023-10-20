import pandas as pd

# Create and slice a Series from a list
# data = [1, 2, 3, 4, 5]
# series1 = pd.Series(data)
# print(series1)
# print(type(series1))
#
# sliced_series1 = series1[1:4]
# print(sliced_series1)

# Create and slice a Series with custom indices
# data = [10, 20, 30, 40, 50]
# custom_indices = ['A', 'B', 'C', 'D', 'E']
# series2 = pd.Series(data, index=custom_indices)
# print(series2)
# sliced_series2 = series2['B':'D']
# print(sliced_series2)

# Creating a dataframe from a dictionary
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'San Francisco', 'Los Angeles']
# }
# df = pd.DataFrame(data)
# print(df)
# print(type(df))

# Creating a dataframe from a list
data1 = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 35, 'Los Angeles']
]
columns = ['Name', 'Age', 'City']
df1 = pd.DataFrame(data1, columns=columns)
print(df1)
print(type(df1))

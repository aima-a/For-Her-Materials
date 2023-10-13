'''Handling csv files involves importing libraries and using for loops'''
# Reading a csv file and accessing its data
import csv
with open("employees_data.csv", 'r') as file:
    content = csv.reader(file)
    print(content)
    for row in content:
        print(row)  # Each row is treated as a list of values

# Appending data to an existing csv file
with open("employees_data.csv", 'a', newline='\n') as file:
    writer = csv.writer(file)
    writer.writerow(['Aima', 'Female', '8/17/87', '3:33 PM', '50000', '10.1', 'FALSE', 'Engineering'])

# Writing data to a new csv file
with open('new_csv_file.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Country"])
    writer.writerow(["John", "25", "USA"])
    writer.writerow(["Mary", "22", "USA"])



'''Handling csv files involves importing libraries and using for loops'''
# Reading a csv file and accessing its data
import csv
with open("file_name.csv", 'r') as file:
    content = csv.reader(file)
    for row in content:
        print(row)  # Each row is treated as a list of values

# Writing data to a csv file
with open("new_file.csv", 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Country"])
    writer.writerow(["John", "25", "USA"])



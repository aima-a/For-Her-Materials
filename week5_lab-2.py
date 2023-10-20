import csv

# Specify the input and output file names
input_file = '/Users/aimaanwar/Documents/PyCharm Projects/For Her/Data/employees_data.csv'
output_file = 'cleaned_data.csv'

# Open the input CSV file and the output CSV file
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Write the header row to the output file
    header = next(reader)
    writer.writerow(header)

    # Define a function to check the validity of a row (customize this for specific data)
    def is_valid_row(row):
        if len(row) == len(header):  # Check if the row has the same number of columns as the header
            # Add additional checks for data validity here if needed
            return True
        return False

    # Iterate through the rows in the input file and write valid rows to the output file
    for row in reader:
        if is_valid_row(row):
            writer.writerow(row)

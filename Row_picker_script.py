import csv

# Define the name of the input and output CSV files
input_file = "Plate_1_luminescence_out_new.csv"
output_file = "output_Selected_rows.csv"

# Define the values to look for in the first column
desired_values = ["D2", "D3", "D4", "D5", "C2", "C3", "C4", "C5"]

# Read the input CSV file
with open(input_file, "r") as csv_file:
    reader = csv.reader(csv_file)
    rows = [row for row in reader]

# Find the rows that match the desired values in the first column
selected_rows = []
for row in rows:
    if row[0] in desired_values:
        selected_rows.append(row)

if not selected_rows:
    print("No rows with the desired values found in the first column.")
else:
    # Transpose the selected rows to write them in columns
    columns = zip(*selected_rows)

    # Write the selected columns to the output CSV file
    with open(output_file, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for column in columns:
            writer.writerow(column)

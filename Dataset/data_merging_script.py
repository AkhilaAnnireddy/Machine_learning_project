import os
import pandas as pd

# Directory containing your CSV files
input_dir = "/Users/akhilaannireddy/Projects/Machine_learning_project/Dataset/users_csv"

# Output file path
output_file = "/Users/akhilaannireddy/Projects/Machine_learning_project/Dataset/merged_users.csv"

# Get a list of all CSV files in the directory
csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

# Initialize an empty list to store dataframes
dataframes = []

# Loop through each CSV file and read it into a dataframe
for csv_file in csv_files:
    file_path = os.path.join(input_dir, csv_file)
    try:
        # Read the CSV file and append to the list
        df = pd.read_csv(file_path)
        dataframes.append(df)
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")

# Concatenate all dataframes
merged_df = pd.concat(dataframes, ignore_index=True)

# Save the merged dataframe to a CSV file
merged_df.to_csv(output_file, index=False)

print(f"All CSV files have been merged and saved to {output_file}")

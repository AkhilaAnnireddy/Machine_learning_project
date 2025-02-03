import os
import pandas as pd

input_dir = "/Users/akhilaannireddy/Projects/Machine_learning_project/Dataset/users_csv"
output_file = "/Users/akhilaannireddy/Projects/Machine_learning_project/Dataset/merged_users.csv"
csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
dataframes = []

for csv_file in csv_files:
    file_path = os.path.join(input_dir, csv_file)
    try:
        df = pd.read_csv(file_path)
        dataframes.append(df)
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")
merged_df = pd.concat(dataframes, ignore_index=True)
merged_df.to_csv(output_file, index=False)

print(f"All CSV files have been merged and saved to {output_file}")

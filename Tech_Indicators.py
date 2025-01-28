import os
import pandas as pd
from stockstats import wrap
from tqdm import tqdm

# Set the path to the folder containing the raw data
input_folder_path = 'data/input'
output_folder_path = 'data/output'

# Create the output folder if it does not exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Get a list of all CSV files in the folder
csv_files = [f for f in os.listdir(input_folder_path) if f.endswith('.csv')]

# Wrap the file list with tqdm to show a progress bar
for filename in tqdm(csv_files, desc='Processing files'):
    try:
        # Construct the full file path
        input_file_path = os.path.join(input_folder_path, filename)
        print(f"Processing file: {input_file_path}")

        # Read the CSV file
        data = pd.read_csv(input_file_path)

        # Standardise column names and rename 'vol' to 'volume'
        data.columns = data.columns.str.strip().str.lower()
        if 'vol' in data.columns:
            data.rename(columns={'vol': 'volume'}, inplace=True)

        # Ensure all required columns are present
        required_columns = {'open', 'high', 'low', 'close', 'volume'}
        for col in required_columns:
            if col not in data.columns:
                print(f"Missing column: {col}. Adding default values.")
                data[col] = 0

        # Process the data using stockstats
        df = wrap(data)
        df.init_all()

        # Get the stock code, assuming the stock code is part of the file name
        stock_code = filename.split('.')[0]

        # Construct the output file path
        output_file_path = os.path.join(output_folder_path, f'{stock_code}.csv')

        # Save the processed data as a CSV file
        df.to_csv(output_file_path, index=False)
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print('All CSV files have been processed and saved.')

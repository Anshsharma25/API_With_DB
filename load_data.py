import os
import pandas as pd

# Define the absolute file path
file_path = r'C:\Users\HP\Desktop\Adme API\data\bank.csv'

# Check if the file exists
if os.path.exists(file_path):
    # Read the CSV file into a pandas DataFrame
    banks_df = pd.read_csv(file_path)
    print("File loaded successfully.")
    # Further processing with banks_df
else:
    # Handle the case where the file is not found
    print(f"Error: File not found at path '{file_path}'. Please check the file path and try again.")
    # Optionally, you can exit the script or perform other error handling steps here
    # For example:
    # exit(1)  # Exit with a non-zero status code indicating error
    # Or raise an exception if appropriate:
    # raise FileNotFoundError(f"File not found: {file_path}")

# load.py
import sys
import pandas as pd

def load_data(file_path):
    file_path = "organization.csv"
    df = pd.read_csv(file_path)
    print(df.head())  # Just to verify the data is loaded
    return df

if __name__ == "__main__":
    file_path = sys.argv[1]  # Take the file path as a command-line argument
    load_data(file_path)


# dpre.py
import sys
import pandas as pd

def data_preprocessing(file_path):
    file_path = "organization.csv"
    df = pd.read_csv(file_path)
    df = df.dropna()
    # Save the processed dataframe to a new CSV file
    df.to_csv('res_dpre.csv', index=False)

if __name__ == "__main__":
    file_path = sys.argv[1]
    data_preprocessing(file_path)

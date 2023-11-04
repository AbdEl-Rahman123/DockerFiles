# eda.py
import sys
import pandas as pd

def exploratory_data_analysis(file_path):
    file_path = "organization.csv"
    df = pd.read_csv(file_path)
    # Perform your EDA here and generate insights
    # For example, print out the summary statistics:
    print(df.describe())
    # Save insights to text files
    with open('eda-in-1.txt', 'w') as f:
        f.write(str(df.describe()))

if __name__ == "__main__":
    file_path = sys.argv[1]
    exploratory_data_analysis(file_path)

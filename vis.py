# vis.py
import sys
import pandas as pd
import matplotlib.pyplot as plt

def create_visualization(file_path):
    file_path = "organization.csv"
    df = pd.read_csv(file_path)
    # Create a histogram of the 'Number of employees' column
    plt.figure(figsize=(10, 6))
    df['Number of employees'].hist(bins=50)  # Adjust the number of bins as needed
    plt.title('Distribution of Number of Employees')
    plt.xlabel('Number of Employees')
    plt.ylabel('Frequency')
    plt.savefig('vis.png')

if __name__ == "__main__":
    file_path = sys.argv[1]
    create_visualization(file_path)


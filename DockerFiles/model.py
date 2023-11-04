# model.py
import sys
import pandas as pd
from sklearn.cluster import KMeans

def k_means_clustering(file_path, k=3):
    file_path = "organization.csv"
    df = pd.read_csv(file_path)
    # Select the columns you want to use for clustering
    X = df[['Country', 'Number of employees']] 
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    df['cluster'] = kmeans.labels_
    # Save the number of records in each cluster
    cluster_counts = df['cluster'].value_counts()
    with open('k.txt', 'w') as f:
        f.write(str(cluster_counts))

if __name__ == "__main__":
    file_path = sys.argv[1]
    k_means_clustering(file_path)

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: A pandas DataFrame containing the data.
    """
    return pd.read_csv(file_path)

def scale_data(data):
    """
    Scale the data using StandardScaler.

    Args:
    - data (pd.DataFrame): Input data to be scaled.

    Returns:
    - np.ndarray: Scaled data.
    """
    scaler = StandardScaler()
    return scaler.fit_transform(data)

def perform_kmeans_clustering(data, n_clusters=4, random_state=42):
    """
    Perform K-means clustering on the input data.

    Args:
    - data (np.ndarray): Scaled data for clustering.
    - n_clusters (int): Number of clusters for K-means.
    - random_state (int): Random state for reproducibility.

    Returns:
    - pd.DataFrame: Data with cluster labels added.
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    cluster_labels = kmeans.fit_predict(data)
    data_with_clusters = data.copy()
    data_with_clusters['Cluster'] = cluster_labels
    return data_with_clusters, kmeans.cluster_centers_

def main():
    # Load the dataset
    usa_arrests_df = load_data('../data/USArrests.csv')

    # Select the variables for clustering
    X = usa_arrests_df[['Murder', 'Assault', 'UrbanPop', 'Rape']]

    # Scale the data
    X_scaled = scale_data(X)

    # Perform K-means clustering with K=4
    clustered_data, cluster_centers = perform_kmeans_clustering(X_scaled)

    # Qualitative description of each cluster
    scaler = StandardScaler()
    cluster_centers_unscaled = scaler.inverse_transform(cluster_centers)
    cluster_labels = ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4']
    for i, center in enumerate(cluster_centers_unscaled):
        print(f"{cluster_labels[i]}:")
        print(f"  - Murder: {center[0]:.2f}")
        print(f"  - Assault: {center[1]:.2f}")
        print(f"  - UrbanPop: {center[2]:.2f}")
        print(f"  - Rape: {center[3]:.2f}")
        print()

if __name__ == '__main__':
    main()

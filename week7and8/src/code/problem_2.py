import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def read_data(file_path):
    """
    Read data from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: A pandas DataFrame containing the data.
    """
    with open(file_path, "r") as infile:
        return pd.read_csv(infile)

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

def euclidean_distance(p, q):
    """
    Calculate the Euclidean distance between two points.

    Args:
    - p (np.ndarray): First point.
    - q (np.ndarray): Second point.

    Returns:
    - float: Euclidean distance between the two points.
    """
    return np.sqrt(np.sum((q - p) ** 2))

def min_similarity(cluster1, cluster2):
    """
    Calculate the minimum similarity between two clusters.

    Args:
    - cluster1 (list): List of points in the first cluster.
    - cluster2 (list): List of points in the second cluster.

    Returns:
    - float: Minimum similarity between the two clusters.
    """
    min_distance = np.inf
    for point1 in cluster1:
        for point2 in cluster2:
            distance = euclidean_distance(point1, point2)
            if distance < min_distance:
                min_distance = distance
    return min_distance

def max_similarity(cluster1, cluster2):
    """
    Calculate the maximum similarity between two clusters.

    Args:
    - cluster1 (list): List of points in the first cluster.
    - cluster2 (list): List of points in the second cluster.

    Returns:
    - float: Maximum similarity between the two clusters.
    """
    max_distance = 0
    for point1 in cluster1:
        for point2 in cluster2:
            distance = euclidean_distance(point1, point2)
            if distance > max_distance:
                max_distance = distance
    return max_distance

def average_similarity(cluster1, cluster2):
    """
    Calculate the average similarity between two clusters.

    Args:
    - cluster1 (list): List of points in the first cluster.
    - cluster2 (list): List of points in the second cluster.

    Returns:
    - float: Average similarity between the two clusters.
    """
    total_distance = 0
    count = 0
    for point1 in cluster1:
        for point2 in cluster2:
            total_distance += euclidean_distance(point1, point2)
            count += 1
    return total_distance / count

def hierarchical_clustering(data, similarity_measure):
    """
    Perform hierarchical clustering on the input data.

    Args:
    - data (np.ndarray): Scaled data for clustering.
    - similarity_measure (function): Function to calculate similarity between clusters.

    Yields:
    - list: List of clusters at each iteration.
    """
    clusters = [[i] for i in range(len(data))]  # Each data point is initially a cluster

    while len(clusters) > 1:
        min_distance = np.inf
        min_indices = None

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                distance = similarity_measure(data[clusters[i]], data[clusters[j]])
                if distance < min_distance:
                    min_distance = distance
                    min_indices = (i, j)

        i, j = min_indices
        new_cluster = clusters[i] + clusters[j]  # Merge clusters
        updated_clusters = [cluster for idx, cluster in enumerate(clusters) if idx not in (i, j)]
        updated_clusters.append(new_cluster)
        clusters = updated_clusters

        yield clusters

def main():
    usa_arrests_df = read_data("../data/USArrests.csv")
    X = usa_arrests_df[['Murder', 'Assault', 'UrbanPop', 'Rape']]
    X_scaled = scale_data(X)

    min_clusters = list(hierarchical_clustering(X_scaled, min_similarity))
    max_clusters = list(hierarchical_clustering(X_scaled, max_similarity))
    average_clusters = list(hierarchical_clustering(X_scaled, average_similarity))

    print("Min similarity measure:")
    for i, clusters in enumerate(min_clusters):
        print(f"Iteration {i + 1}: Number of clusters = {len(clusters)}")

    print("\nMax similarity measure:")
    for i, clusters in enumerate(max_clusters):
        print(f"Iteration {i + 1}: Number of clusters = {len(clusters)}")

    print("\nAverage similarity measure:")
    for i, clusters in enumerate(average_clusters):
        print(f"Iteration {i + 1}: Number of clusters = {len(clusters)}")

if __name__ == "__main__":
    main()

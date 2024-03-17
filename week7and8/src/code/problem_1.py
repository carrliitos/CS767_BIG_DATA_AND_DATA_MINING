import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    # Load the dataset
    usa_arrests_df = pd.read_csv('../data/USArrests.csv')

    # Select the variables for clustering
    X = usa_arrests_df[['Murder', 'Assault', 'UrbanPop', 'Rape']]

    # Scale the data
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Perform K-means clustering with K=4
    kmeans = KMeans(n_clusters=4, random_state=42)
    usa_arrests_df['Cluster'] = kmeans.fit_predict(X_scaled)

    # Qualitative description of each cluster
    cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
    cluster_labels = ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4']
    for i, center in enumerate(cluster_centers):
        print(f"{cluster_labels[i]}:")
        print(f"  - Murder: {center[0]:.2f}")
        print(f"  - Assault: {center[1]:.2f}")
        print(f"  - UrbanPop: {center[2]:.2f}")
        print(f"  - Rape: {center[3]:.2f}")
        print()

if __name__ == '__main__':
    main()

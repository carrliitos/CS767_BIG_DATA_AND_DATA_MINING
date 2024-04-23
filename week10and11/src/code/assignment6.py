import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

current_file_path = os.path.abspath(__file__)
current_dir = os.path.abspath(os.path.join(current_file_path, os.pardir))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

def myPCA(data):
  cov_matrix = np.cov(data, rowvar=False)
  latent, coeff = np.linalg.eig(cov_matrix)
  latent = np.real(latent)
  coeff = np.real(coeff)
  idx = np.argsort(-latent)
  latent = latent[idx]
  coeff = coeff[:, idx]

  return coeff, latent

def eigenfaces(data):
  coeff, _ = myPCA(data)
  for i in range(5):
    eigen_face_image = coeff[:, i].reshape(30, 32)
    plt.imshow(eigen_face_image, cmap='gray')
    plt.title(f'Eigenface {i+1}')
    plt.axis('off')
    plt.savefig(f'{parent_dir}/imgs/eigenface_{i+1}.png')
    plt.close()

def ProportionOfVariance(training_data):
  coeff, latent = myPCA(training_data)
  total_variance = np.sum(latent)
  variance_explained = [(latent[i] / total_variance) for i in range(len(latent))]
  cumulative_variance = np.cumsum(variance_explained)
  k = np.argmax(cumulative_variance >= 0.90) + 1  # Add 1 to get the number of eigenvectors
  plt.plot(cumulative_variance)
  plt.xlabel('Number of Principal Components')
  plt.ylabel('Cumulative Proportion of Variance Explained')
  plt.title('Cumulative Proportion of Variance Explained by Principal Components')
  plt.axvline(x=k, color='r', linestyle='--', label=f'90% Variance Explained (k={k})')
  plt.legend()
  plt.grid()
  plt.show()
  return k

def project_data(data, coeff, k):
  return np.dot(data, coeff[:, :k])

def main():
  train_data = np.loadtxt(f'{parent_dir}/data/face_train_data_960.txt')
  test_data = np.loadtxt(f'{parent_dir}/data/face_test_data_960.txt')

  X_train, y_train = train_data[:, :-1], train_data[:, -1]
  X_test, y_test = test_data[:, :-1], test_data[:, -1]

  # Part a: Implement myPCA function
  coeff, latent = myPCA(X_train)

  # Part b: Create eigenfaces
  # eigenfaces(X_train)

  # Part c: Generate plot of proportion of variance
  # k = ProportionOfVariance(X_train)

  # Part d: Project training and test data
  # k_values = [1, 3, 5, 7]
  # for k_value in k_values:
  #   PX_train = project_data(X_train, coeff, k_value)
  #   PX_test = project_data(X_test, coeff, k_value)

  #   # Run kNN
  #   knn = KNeighborsClassifier()
  #   knn.fit(PX_train, y_train)
  #   y_pred = knn.predict(PX_test)
  #   accuracy = accuracy_score(y_test, y_pred)
  #   print(f"Accuracy for k={k_value}: {accuracy}")

  # Part e: Approximate the first five images in the training set
  for k in [50, 100]:
    train_pca = np.dot(X_train, coeff[:, :k])
    reconstructed_train = np.dot(train_pca, coeff[:, :k].T)
    fully_reconstructed_train = reconstructed_train + np.mean(X_train, axis=0)

    # Display the images
    fig, axes = plt.subplots(1, 5, figsize=(15, 3))
    for i in range(5):
      axes[i].imshow(fully_reconstructed_train[i].reshape(30, 32), cmap='gray')
      axes[i].axis('off')
    plt.show()

if __name__ == "__main__":
  main()

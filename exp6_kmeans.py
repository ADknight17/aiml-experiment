from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1,2],[1.5,1.8],[5,8],[8,8]])

model = KMeans(n_clusters=2)
model.fit(X)

print("Labels:", model.labels_)
print("Centroids:", model.cluster_centers_)
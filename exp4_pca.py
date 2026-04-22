from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

data = load_iris()
X = data.data

pca = PCA(n_components=2)
X_new = pca.fit_transform(X)

print("Original:", X.shape)
print("Reduced:", X_new.shape)
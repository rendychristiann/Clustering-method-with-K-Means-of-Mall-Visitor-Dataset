# TUGAS 3 PEMODELAN DAN PEMBELAJARAN MESIN
# NAMA : RENDY CHRISTAN
# NPM  : 2006529695
# CLUSTERING K- MEANS DENGAN LIBRARY SKLEARN PADA DATASET DATA PENGUNJUNG MALL

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# import dataset
df = pd.read_csv ('C:/Users/OSMOND/Documents/Python/dataPengunjungMall.csv')
df.head()
print(df.head())

# Making  the independent variables matrix
X = df.iloc[:, [3, 4]].values # membuat matriks untuk independent variable (features)
df = pd.get_dummies(df, columns = ['Gender'], prefix = ['Gender']) 
# melakukan one hot encoding untuk mengategorikan data gender

# clustering
wcss = []       # buat matriks WCSS
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++')
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# mengeplot grafik elbow method
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Jumlah clusters')
plt.ylabel('WCSS')
plt.show()

#Taking number of clusters = 5
kmeans = KMeans(n_clusters = 5, init = 'k-means++')
y_kmeans = kmeans.fit_predict(X)

# PLotting the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 25, c = 'black', label = 'k - 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 25, c = 'green', label = 'k - 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 25, c = 'blue', label = 'k - 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 25, c = 'red', label = 'k - 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 25, c = 'yellow', label = 'k - 5')
plt.title('Cluster Pelanggan', size = 15)
plt.xlabel('Pendapatan Tahunan(k$)', size = 10)
plt.ylabel('Tingkat penjualan (1-100)', size = 10)
plt.legend()
plt.show()
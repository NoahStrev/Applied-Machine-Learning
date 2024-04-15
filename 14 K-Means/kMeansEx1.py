import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('AZ_mall_shoppers.csv')
print('\nDATA:')
print(data.info())

# Standardize the dataa
X = StandardScaler().fit_transform(data)

# LOOK FOR OPTIMAL K
from sklearn.cluster import KMeans
meas = []
for i in range(1,12):
    kmeans = KMeans(n_clusters=i,random_state=42)
    kmeans.fit(X)
    meas.append(kmeans.inertia_)

plt.plot(range(1,12), meas)
plt.xlabel('Number of clusters')
plt.ylabel('MEAS')
plt.show()

# NOTE Elbow method indicates that the number of clusters should be 5
# but could try 3 as well

# Create the ML model
#km = KMeans(n_clusters=5,max_iter=300,random_state=42)
km = KMeans(n_clusters=3,max_iter=300,random_state=42)
km.fit(X)
print('\nCentroids')
print(km.cluster_centers_)
print('cluser to which samples belong:')
print(km.labels_)
print(len(km.labels_))

# Let's graph
plt.scatter(X[km.labels_==0,0], X[km.labels_==0,1], c='green', label='cluster 1')
plt.scatter(X[km.labels_==1,0], X[km.labels_==1,1], c='blue', label='cluster 2')
plt.scatter(X[km.labels_==2,0], X[km.labels_==2,1], c='red', label='cluster 3')
##plt.scatter(X[km.labels_==3,0], X[km.labels_==3,1], c='yellow', label='cluster 4')
##plt.scatter(X[km.labels_==4,0], X[km.labels_==4,1], c='violet', label='cluster 5')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],
            c='black', label='Centroids')
plt.legend()
plt.show()


































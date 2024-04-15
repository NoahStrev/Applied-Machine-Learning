# Text Clustering
import json
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_json('sampleposts.json')
# Extract the headlines as sentences
sentence = df.headline

vectorizer= TfidfVectorizer(stop_words='english')

#vectorizer the text
vectorized_docs = vectorizer.fit_transform(sentence)
print(vectorized_docs)

pca = PCA(n_components=2)
reduced_data = pca.fit_transform(vectorized_docs.toarray())

print('PCA reduced dimensionality on our data:')
print(reduced_data)

#cluster the blog posts (docs)
num_clusters = 2
kmeans = KMeans(n_clusters=num_clusters, n_init=5, max_iter=500,
                random_state=42)
kmeans.fit(reduced_data)

# create a dataframe to store the results
results = pd.DataFrame()
results['document'] = sentence
results['cluster'] = kmeans.labels_

pd.options.display.max_rows=None
print(results)

# plot the results
colors=['red','blue']
for i in range(num_clusters):
    plt.scatter(reduced_data[kmeans.labels_ == i,0],
                reduced_data[kmeans.labels_ == i,1],
                s=10,
                color=colors[i],
                label='cluster'+str(i))
plt.legend()
plt.show()

    




















































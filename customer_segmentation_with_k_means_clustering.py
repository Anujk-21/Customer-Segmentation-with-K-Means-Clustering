# -*- coding: utf-8 -*-
"""Customer Segmentation with K-Means Clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PGFbZgFCUt4gvmrMGh-OG_16JF72VPir
"""

#importing lib for data analytics

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from google.colab import files
up = files.upload()

df = pd.read_csv('Customers.csv')

df.head()

df.describe()

df.info()

df.shape

df.plot(x='Age', y='Annual Income (k$)', style='*',xlabel = "Annual Income", ylabel = "Age", color = "red")

X  = df.iloc[:,[3,4]].values

X

#importing lib for Clustering
from sklearn.cluster import KMeans
clst = []

for i in range(1,11):
  kmeans = KMeans(n_clusters = i, init='k-means++', random_state=0)
  kmeans.fit(X)
  clst.append(kmeans.inertia_)

plt.plot(range(1,11),clst)
plt.title("Elbow Method")
plt.xlabel("No. of clusters")
plt.ylabel("clst volume")
plt.show()

#from the above graph we got to know that elbow methos points on 5 Clusters

#mode
kmeansmodel = KMeans(n_clusters = 5, init = 'k-means++',random_state=0)

y__kmeans =kmeansmodel.fit_predict(X)

plt.scatter(X[y__kmeans == 0,0],X[y__kmeans == 0,1], s= 80, c= "cyan",label = 'Customer 1' )
plt.scatter(X[y__kmeans == 1,0],X[y__kmeans == 1,1], s= 80, c= "red",label = 'Customer 2' )
plt.scatter(X[y__kmeans == 2,0],X[y__kmeans == 2,1], s= 80, c= "yellow",label = 'Customer 3' )
plt.scatter(X[y__kmeans == 3,0],X[y__kmeans == 3,1], s= 80, c= "purple",label = 'Customer 4' )
plt.scatter(X[y__kmeans == 4,0],X[y__kmeans == 4,1], s= 80, c= "green",label = 'Customer 5' )
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 100, c = 'black', label= 'centroids')
plt.title("clusters of customers")
plt.xlabel("Annual Income(k$)")
plt.ylabel("Spending score(1-100)")
plt.legend()
plt.show()

#Red area clusters are very targeted for market place
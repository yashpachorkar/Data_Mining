# Question 2(c)
import numpy as np 
import pandas as pd 
import random as rd
import matplotlib.pyplot as plt
from math import sqrt


data = pd.read_csv(r'C:\AnnacondaProjects\Anna Projects\Homework 3\faithful.csv')
data.head()

X = data[["eruptions", "waiting"]]

plt.scatter(X["eruptions"], X["waiting"], c="blue")
plt.xlabel("eruptions")
plt.ylabel("waiting")
plt.show()


K=2


Centroids = (X.sample(n=K))
plt.scatter(X["eruptions"], X["waiting"], c="blue")
plt.scatter(Centroids["eruptions"], Centroids["waiting"], c="red")
plt.xlabel("eruptions")
plt.ylabel("waiting")
plt.show()


Centroids

diff = 1
j=0

while(diff!=0):
    XD=X
    i=1
    for index1, row_c in Centroids.iterrows():
        ED=[]
        for index2, row_d in XD.iterrows():
            d1 = (row_c["eruptions"]-row_d["eruptions"])**2
            d2 = (row_c["waiting"]-row_d["waiting"])**2
            d = sqrt(d1+d2)
            ED.append(d)
        X[i] = ED
        i = i+1
    
    C = []
    for index, row in X.iterrows():
        min_dist=row[1]
        pos=1
        for i in range(K):
            if row[i+1] < min_dist:
                min_dist = row[i+1]
                pos = i+1
        C.append(pos)
    X["Cluster"]=C
    Centroids_new = X.groupby(["Cluster"]).mean()[["waiting", "eruptions"]]
    if j == 0:
        diff = 1
        j = j+1
    else:
        diff = (Centroids_new['waiting'] - Centroids['waiting']).sum() + (Centroids_new['eruptions'] - Centroids['eruptions']).sum()
        print(diff.sum())
    Centroids = X.groupby(["Cluster"]).mean()[["waiting","eruptions"]]
    
    
color=['blue','green','cyan']
for k in range(K):
    data=X[X["Cluster"]==k+1]
    plt.scatter(data["eruptions"],data["waiting"],c=color[k])
plt.scatter(Centroids["eruptions"],Centroids["waiting"],c='red')
plt.xlabel('eruptions')
plt.ylabel('waiting')
plt.show()

wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init='k-means++', max_iter=300, n_init = 10, random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('objective vs iteration')
plt.xlabel('iteration')
plt.ylabel('objective')

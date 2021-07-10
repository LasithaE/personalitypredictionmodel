import pandas as pd
import numpy as np
import pickle
from sklearn.cluster import MiniBatchKMeans
df = pd.read_csv("data-final.csv", delimiter="\t")
columns = df.columns #['EXT1','EXT2'....]
x = df[df.columns[0:50]]
x = x.fillna(0) #NaN
kmeans = MiniBatchKMeans(n_clusters=10,random_state=0,batch_size=100,max_iter=100).fit(x)


pickle.dump(kmeans.cluster_centers_,open('model.pkl','wb'))
model=pickle.load(open('model.pkl','rb'))
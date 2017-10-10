from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.datasets import load_files
import time
import os
start_time = time.time()

dataset =[]
filecontent = []
path ='./txt'
files = [f for f in os.listdir(path) if os.path.split(f)]
for f in files:
	if f.endswith(".txt"):
		filecontent.append(f)
#Vamos a ver como pasar el contenido del txt para poder analizarlo

for f in filecontent:
	j = os.path.join(path, f)
	with open(j, 'r') as myfile:
		data=myfile.read().replace('\n', '')
		dataset.append(data)

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(dataset)
 
true_k = 4
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1,n_jobs=-2)
model.fit(X)
 
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print
 
 
print("\n")
print("The execution time was %s seconds" % (time.time() - start_time))
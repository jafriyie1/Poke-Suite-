from sklearn.cluster import KMeans
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from matplotlib import pyplot as plt
import numpy as np
import pickle
import time

start = time.time()
df = pd.read_json("/Users/Joel/Desktop/Tweets/final_poke_tweets.json")
text_data = df["text"].fillna('')

vect = TfidfVectorizer(stop_words='english')
final_text_data = vect.fit_transform(text_data)

true_k = 5
model = pickle.load(open('/Users/Joel/Desktop/Tweets/kmeans.pkl', 'rb+'))

print('Top terms per cluster:')
order_centroids = model.cluster_centers_.argsort()[:,::-1]
terms = vect.get_feature_names()

f = open('Top10Cluster.txt', 'w')
f.write("Top ten terms per cluster. \n")

print("Top ten terms per cluster.")
for i in range(true_k):
    print("Cluster %d: " % i)
    f.write("Cluster"+str(i)+": \n")
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
        f.write(' '+str(terms[ind])+'\n')
    f.write('\n')
    print

f.close()
print()
'''labels = model.labels_
centroids = model.cluster_centers_
print('Now we will visualize....')


for i in range(true_k):
    # select only the data that matches with
    # cluster label == i
    sample = np.array(final_text_data[np.where(labels==i)])
    #print(type(sample[:,2]))
    #plot the data observation
    print(sample)
    #plt.plot(sample[0], sample[1],'o')
    #plot the centroids
    lines = plt.plot(centroids[i,0], centroids[i,1], 'kx')
    # make the centroid x's slightly bigger
    plt.setp(lines, ms=20.0)
    plt.setp(lines, mew=3.0)
#plt.show()
final_time = time.time() - start
print('The program ran in: %s' % final_time )
'''

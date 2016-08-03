'''Unsupervised learning analysis on Twitter Data'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import pickle

df = pd.read_json("/Users/Joel/Desktop/Tweets/final_poke_tweets.json")
text_data = df["text"].fillna('')

vect = TfidfVectorizer(stop_words='english')
final_text_data = vect.fit_transform(text_data)

print('Training....')
true_k = 5
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(final_text_data)

print('Top terms per cluster:')
order_centroids = model.cluster_centers_.argsort()[:,::-1]
terms = vect.get_feature_names()
for i in range(true_k):
    print("Cluster %d: " % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print

f = pickle.dump(model, open('/Users/Joel/Desktop/Tweets/kmeans.pkl','wb'))
print('done')

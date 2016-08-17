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

f = pickle.dump(model, open('/Users/Joel/Desktop/Tweets/kmeans.pkl','wb'))

print('Done.')

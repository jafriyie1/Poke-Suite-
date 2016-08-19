from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import pickle
from io import StringIO

df = pd.read_json("/Users/Joel/Desktop/Tweets/final_poke_tweets.json")
text_data = df["text"].fillna('')

pred_tweet = "Niantic Labs has made a public statement regarding their recent banning of accounts in"


vect = TfidfVectorizer(stop_words='english')
vec = vect.fit_transform(text_data)

final_pred_data = vect.transform(pred_tweet.split('\n'))


model = pickle.load(open('/Users/Joel/Desktop/Tweets/kmeans.pkl', 'rb+'))

prediction = model.predict(final_pred_data)

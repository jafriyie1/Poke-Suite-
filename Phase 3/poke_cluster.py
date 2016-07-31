'''Unsupervised learning analysis on Twitter Data'''
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

df = pd.read_json("/Users/Joel/Desktop/Tweets/final_poke_tweets.json")
text_data = df["text"].fillna('')

count_vect = CountVectorizer()
final_text_data = count_vect.fit_transform(text_data)
count_vect.vocabulary_.get('Pokemon')

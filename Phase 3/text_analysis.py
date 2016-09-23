"""Text analysis in Python"""

import pandas as pd
import nltk
from nltk.corpus import stopwords



stop = stopwords.words('english')
df = pd.read_json("/Users/Joel/Desktop/Tweets/final_poke_tweets.json")

def transform_data_for_processing(data):
    #Transforms twiiter data into a list of words
    #And removes stop words
    alist = []
    temp = ""
    for x in range(len(data)):
        temp = str(data[x]).lower()
        adj_temp = [i for i in temp if i not in stop]
        alist.append(temp.split())
    return alist


"""Columns
'contributors', 'coordinates', 'created_at', 'entities',
       'extended_entities', 'favorite_count', 'favorited', 'filter_level',
       'geo', 'id', 'id_str', 'in_reply_to_screen_name',
       'in_reply_to_status_id', 'in_reply_to_status_id_str',
       'in_reply_to_user_id', 'in_reply_to_user_id_str', 'is_quote_status',
       'lang', 'limit', 'place', 'possibly_sensitive', 'quoted_status',
       'quoted_status_id', 'quoted_status_id_str', 'retweet_count',
       'retweeted', 'retweeted_status', 'scopes', 'source', 'text',
       'timestamp_ms', 'truncated', 'user']
"""


text_data = df["text"]

#print((text_data[1]))

transformed_text_data = transform_data_for_processing(text_data)
transformed_tokenize_list = tokenize_data(transformed_text_data)


for line in transformed_tokenize_list:
    print(line)

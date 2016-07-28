"""Converting text into JSON object"""
import json

tweets = []

poke_tweet  = open("/Users/Joel/Desktop/Tweet Data/poke_tweets.txt", "r")

for line in poke_tweet:
    try:
        tweet = json.loads(line)
        tweets.append(tweet)
    except:
        continue


poke_tweet.close()
with open("final_poke_tweets.json", "w") as objectfile:
    json.dump(tweets, objectfile, indent=4)

print("Done")

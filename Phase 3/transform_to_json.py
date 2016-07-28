"""Converting text into JSON object"""
import json

tweets = []

poke_tweet  = open("poke_tweets.txt", "r")

for line in poke_tweet:
    try:
        tweet = json.loads(line)
        tweets.append(tweet)
    except:
        continue


poke_tweet.close()
poke_tweet_two = open("poke_tweets_two.txt", "r")
for line in poke_tweet_two:
    try:
        tweet = json.loads(line)
        tweets.append(tweet)
    except:
        continue

poke_tweet_two.close()

with open("final_poke_tweets.json", "w") as objectfile:
    json.dump(tweets, objectfile, indent=4)

print("Done")

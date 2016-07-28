#Import the necessary methods from tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json


def values():
    access_token = input("Please input access_token: ")
    access_token_secret = input("Please input access_secret_token: ")
    consumer_key = input("Please input consumer_key: ")
    consumer_secret = input("Please input consumer_secret: ")
    return(access_token, access_token_secret, consumer_key, consumer_secret)

#Basic Listener

class StdOutListener(StreamListener):

    def on_data(self, data):
        #print data
        with open("/Users/Joel/Desktop/Tweet Data/poke_tweets.txt", "w") as text_file:
            text_file.write(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    #This handles Twitter Auth
    data = []
    try:
        access_token, access_token_secret, consumer_key, consumer_secret = values()
        listener = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, listener)

        #This line filters twitter Streams to caputre keywords
        data.append(stream.filter(track=["Pokemon Go", "pokemon", "Pokemon"], languages=["en"]))
    except KeyboardInterrupt:
        #Press Control-C
            pass

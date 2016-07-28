#Import the necessary methods from tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json




#Basic Listener

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    #This handles Twitter Auth
    access_token = input("Please input access_token: ")
    access_token_secret = input("Please input access_secret_token: ")
    consumer_key = input("Please input consumer_key: ")
    consumer_secret = input("Please input consumer_secret: ")

    try:
        listener = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, listener)

        #This line filters twitter Streams to caputre keywords
        stream.filter(track=["Pokemon Go", "pokemon", "Pokemon"])
    except KeyboardInterrupt:
        #Press Control-C
        pass

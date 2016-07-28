#Import the necessary methods from tweepy

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

#Variables for access


access_token = "702882031500308480-FEkkuJZElvOri8xn75RuUUbKS2AujJR"
access_token_secret = "c2pJvG1CFYS74VBcNfkfT5FZzVwdO1Ft2rBfbneyBvvuP"
consumer_key = "Tc1cnYxACqTA2vEESjFZKgrYd"
consumer_secret = "I5vPI2bWEZ8MdCoitS34dR4vbkZydq49jZToXwz6saNi184v6Q"

#Basic Listener

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == "__main__":
    #This handles Twitter Auth
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

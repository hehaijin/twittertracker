#this file runs on Python 2
#captures in real time the tweets contains the keyworkds.
#run python twitterstreamer.py >> output.txt in windows to get output file.
# or python twitterstreamer.py | output.txt in Linux


from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

access_token = "2873038325-Bxf13OncrMdbtBXLjQiy9qYzBTdPRllaElYGhj0"
access_token_secret = "1UUZcGQmpZmq1TaDxbV9eNMnoJdRHER6CqwzDB94BtWjG"
consumer_key = "9PZMpfBWonShNNx3RVA24GR4d"
consumer_secret = "vDHDzT1eQKAqNRRfJ4SOqzEjdeizKHfx46Iq06cO7rhcvJopZC"


class StdOutListener(StreamListener):
    def __init__(self):
        self.count=0


    def on_data(self, data):
        self.count=self.count+1
        #if self.count%100==0:
        #print self.count
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['trump'])

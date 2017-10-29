import json
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

tweets_data_path = './output.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "rb")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        #print(tweet.get("text"))
        tweets_data.append(tweet)
    except:
        continue

print(len(tweets_data))


for i in range(100):
	a=TextBlob(tweets_data[i]["text"])
	#print(a)
	#print(a.sentiment.polarity)


tweets = pd.DataFrame()

def getSentiment(tweet):
	a=TextBlob(tweet)
	p=a.sentiment.polarity
	if p>0:
		return 1
	elif p<0:
		return -1
	else: return 0
	



#get an exception because of null value.
tweets['text'] = list(map(lambda tweet:tweet.get("text","null"), tweets_data))
tweets['lang'] =list(map(lambda tweet:tweet.get("lang","null"), tweets_data))
tweets['sentiment']=list(map(lambda tweet:getSentiment(tweet.get("text","null")), tweets_data))
tweets['userid'] = list(map(lambda tweet: tweet.get("user",{}).get("id","null"), tweets_data))
tweets['position'] = list(map(lambda tweet: tweet.get("user",{}).get("position","null"), tweets_data))

#tweets['userdesc'] =list( map(lambda tweet: tweet['user']["description"], tweets_data))
#tweets['followerscount'] =list( map(lambda tweet: tweet.get("user",{})get("followerscount","null"), tweets_data))


tweets_by_sentiment = tweets['sentiment'].value_counts()

print(tweets_by_sentiment)
#for a in tweets_by_sentiment:
#	print(a)

df=tweets.groupby(["userid"]).mean()
print(df)
#df2=df.apply(lambda row: 1 if row["sentiment"]>0 else ( -1 if row["sentiment"]<0 else 0  )  ,axis=1)

df3=df["sentiment"].value_counts()

print(df3)


fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
df[0:5].plot(ax=ax, kind='bar', color='red')

plt.show()



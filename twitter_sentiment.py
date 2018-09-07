from textblob import TextBlob
import tweepy
import csv
import matplotlib.pyplot as plt

#GO TO https://developer.twitter.com TO GET THIS DATA
consumer_key ='CONSUMER_KEY_HERE'
consumer_secret ='CONSUMER_SECRET_HERE'

access_token = 'ACCESS_TOKEN_HERE'
access_token_secret = 'ACCESS_TOKEN_SECRET_HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

pos = 0
neu = 0
neg = 0

positive = []
neutral = []
negative = []

tweet_s = str(raw_input("Tweet to sheare: "))
public_tweets = api.search(tweet_s, count=90)
with open('tweets_sentiment.csv','w') as file:

    for tweet in public_tweets:
        text_tweet = TextBlob(tweet.text)
        print(text_tweet)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
        if analysis.sentiment.polarity > 0:
            sent = "Positive"
            pos += 1
        elif analysis.sentiment.polarity == 0:
            sent = "Neutral"
            neu += 1
        elif analysis.sentiment.polarity < 0:
            sent = "Negative"
            neg += 1

        file.write('%s,  %s\n' % (tweet.text.encode("utf-8"), sent))
        print("")

labels = 'Positive', 'Neutral', 'Negative'
sizes = [pos, neu, neg]
explode = (0, 0.1, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.title('People opinion on ' + tweet_s + '\n')
plt.show()

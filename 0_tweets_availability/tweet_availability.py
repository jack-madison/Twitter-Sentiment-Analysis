import pandas as pd
import time
import tweepy

# If this code has been downloaded from github, please create a new Python file called
# twitter_authentication containing bearer_token = "INSERT YOUR BEARER TOKEN HERE" in the
# same directory as this Python file 
from twitter_authentication import bearer_token_1

client = tweepy.Client(bearer_token_1, wait_on_rate_limit=True)

tweets = []

for response in tweepy.Paginator(client.get_all_tweets_count, 
                                query = '-is:retweet -is:nullcast has:geo place_country:JP',
                                start_time = '2006-03-22T00:00:00+09:00',
                                end_time = '2019-06-30T23:59:59+09:00',
                                granularity = 'hour'):
    time.sleep(1)
    tweets.append(response)

result = []

# Loop through each response object
for response in tweets:
    for tweet in response.data:
        try:
            # Put all of the information we want to keep in a single dictionary for each tweet
            result.append({
                    'start': tweet['start'],
                    'tweet_count': tweet['tweet_count']
                    })
        except TypeError:
            pass
        except KeyError:
            pass
# Change this list of dictionaries into a dataframe
df = pd.DataFrame(result)

df['start'] = pd.to_datetime(df['start'])
df['start'] = df['start'].dt.tz_convert('Japan')

df['date'] = df['start'].dt.date

df = df[['date', 'tweet_count']]

df = df.groupby(['date'], as_index=False)['tweet_count'].sum()

df.to_csv('./0_tweets_availability/tweet_counts.csv', index = False)
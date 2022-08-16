import pandas as pd
import numpy as np
import pytz

# Import all of the data for 2018
tweets_feb = pd.read_csv('./1_tweets_raw/2018/02_2018.csv')
tweets_mar = pd.read_csv('./1_tweets_raw/2018/03_2018.csv')
tweets_apr = pd.read_csv('./1_tweets_raw/2018/04_2018.csv')
tweets_may = pd.read_csv('./1_tweets_raw/2018/05_2018.csv')
tweets_jun = pd.read_csv('./1_tweets_raw/2018/06_2018.csv')

# Concatinate the data into one dataframe
tweets = pd.concat([tweets_feb, tweets_mar, tweets_apr, tweets_may, tweets_jun], axis = 0, join = 'outer')

# Remove duplicate tweets that could show up in the data collection process
tweets = tweets.drop_duplicates()

# Import the location dataset
locations = pd.read_csv('https://media.githubusercontent.com/media/jack-madison/Tweet-Data/main/locations/matched_locations.csv')

# Add the tweet location data to the tweets data
tweets = pd.merge(tweets, locations, how = 'left', on = 'tweet_location_id')

# Remove tweets where there is no municipality attached
tweets = tweets[tweets['mun_id'].notna()]

# Remove tweets where the associated location is an administration or a country
tweets = tweets[(tweets['place_type'] != 'admin') & (tweets['place_type'] != 'country')]

# Reformat the time so that it is in local Japanese time
tweets['tweet_created_at'] = pd.to_datetime(tweets['tweet_created_at'])
tweets['tweet_created_at'] = tweets['tweet_created_at'].dt.tz_convert('Japan')

# Remove the Unnamed: 0 column
tweets = tweets.drop(columns = 'Unnamed: 0')

tweets_feb_w1 = tweets.loc[(tweets['tweet_created_at'] >= '2018-02-01') & (tweets['tweet_created_at'] < '2018-02-08')]
tweets_feb_w2 = tweets.loc[(tweets['tweet_created_at'] >= '2018-02-08') & (tweets['tweet_created_at'] < '2018-02-14')]
tweets_feb_w3 = tweets.loc[(tweets['tweet_created_at'] >= '2018-02-14') & (tweets['tweet_created_at'] < '2018-02-21')]
tweets_feb_w4 = tweets.loc[(tweets['tweet_created_at'] >= '2018-02-21') & (tweets['tweet_created_at'] < '2018-03-01')]

tweets_feb_w1.to_csv('./2_tweets_cleaned/2018/feb_w1_2018.csv', index = False)
tweets_feb_w2.to_csv('./2_tweets_cleaned/2018/feb_w2_2018.csv', index = False)
tweets_feb_w3.to_csv('./2_tweets_cleaned/2018/feb_w3_2018.csv', index = False)
tweets_feb_w4.to_csv('./2_tweets_cleaned/2018/feb_w4_2018.csv', index = False)

tweets_mar_w1 = tweets.loc[(tweets['tweet_created_at'] >= '2018-03-01') & (tweets['tweet_created_at'] < '2018-03-08')]
tweets_mar_w2 = tweets.loc[(tweets['tweet_created_at'] >= '2018-03-08') & (tweets['tweet_created_at'] < '2018-03-14')]
tweets_mar_w3 = tweets.loc[(tweets['tweet_created_at'] >= '2018-03-14') & (tweets['tweet_created_at'] < '2018-03-21')]
tweets_mar_w4 = tweets.loc[(tweets['tweet_created_at'] >= '2018-03-21') & (tweets['tweet_created_at'] < '2018-04-01')]

tweets_mar_w1.to_csv('./2_tweets_cleaned/2018/mar_w1_2018.csv', index = False)
tweets_mar_w2.to_csv('./2_tweets_cleaned/2018/mar_w2_2018.csv', index = False)
tweets_mar_w3.to_csv('./2_tweets_cleaned/2018/mar_w3_2018.csv', index = False)
tweets_mar_w4.to_csv('./2_tweets_cleaned/2018/mar_w4_2018.csv', index = False)

tweets_apr_w1 = tweets.loc[(tweets['tweet_created_at'] >= '2018-04-01') & (tweets['tweet_created_at'] < '2018-04-08')]
tweets_apr_w2 = tweets.loc[(tweets['tweet_created_at'] >= '2018-04-08') & (tweets['tweet_created_at'] < '2018-04-14')]
tweets_apr_w3 = tweets.loc[(tweets['tweet_created_at'] >= '2018-04-14') & (tweets['tweet_created_at'] < '2018-04-21')]
tweets_apr_w4 = tweets.loc[(tweets['tweet_created_at'] >= '2018-04-21') & (tweets['tweet_created_at'] < '2018-05-01')]

tweets_apr_w1.to_csv('./2_tweets_cleaned/2018/apr_w1_2018.csv', index = False)
tweets_apr_w2.to_csv('./2_tweets_cleaned/2018/apr_w2_2018.csv', index = False)
tweets_apr_w3.to_csv('./2_tweets_cleaned/2018/apr_w3_2018.csv', index = False)
tweets_apr_w4.to_csv('./2_tweets_cleaned/2018/apr_w4_2018.csv', index = False)

tweets_may_w1 = tweets.loc[(tweets['tweet_created_at'] >= '2018-05-01') & (tweets['tweet_created_at'] < '2018-05-08')]
tweets_may_w2 = tweets.loc[(tweets['tweet_created_at'] >= '2018-05-08') & (tweets['tweet_created_at'] < '2018-05-14')]
tweets_may_w3 = tweets.loc[(tweets['tweet_created_at'] >= '2018-05-14') & (tweets['tweet_created_at'] < '2018-05-21')]
tweets_may_w4 = tweets.loc[(tweets['tweet_created_at'] >= '2018-05-21') & (tweets['tweet_created_at'] < '2018-06-01')]

tweets_may_w1.to_csv('./2_tweets_cleaned/2018/may_w1_2018.csv', index = False)
tweets_may_w2.to_csv('./2_tweets_cleaned/2018/may_w2_2018.csv', index = False)
tweets_may_w3.to_csv('./2_tweets_cleaned/2018/may_w3_2018.csv', index = False)
tweets_may_w4.to_csv('./2_tweets_cleaned/2018/may_w4_2018.csv', index = False)

tweets_jun_w1 = tweets.loc[(tweets['tweet_created_at'] >= '2018-06-01') & (tweets['tweet_created_at'] < '2018-06-08')]
tweets_jun_w2 = tweets.loc[(tweets['tweet_created_at'] >= '2018-06-08') & (tweets['tweet_created_at'] < '2018-06-14')]
tweets_jun_w3 = tweets.loc[(tweets['tweet_created_at'] >= '2018-06-14') & (tweets['tweet_created_at'] < '2018-06-21')]
tweets_jun_w4 = tweets.loc[(tweets['tweet_created_at'] >= '2018-06-21') & (tweets['tweet_created_at'] < '2018-07-01')]

tweets_jun_w1.to_csv('./2_tweets_cleaned/2018/jun_w1_2018.csv', index = False)
tweets_jun_w2.to_csv('./2_tweets_cleaned/2018/jun_w2_2018.csv', index = False)
tweets_jun_w3.to_csv('./2_tweets_cleaned/2018/jun_w3_2018.csv', index = False)
tweets_jun_w4.to_csv('./2_tweets_cleaned/2018/jun_w4_2018.csv', index = False)
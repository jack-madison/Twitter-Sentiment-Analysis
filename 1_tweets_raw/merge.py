# The following python code merges the tweet data. I decided to pull the data in smaller
# batches to aviod going over the rate limit and losing the entire dataframe.
import pandas as pd
import numpy as np

week1 = pd.read_csv('./1_tweets_raw/2017/jun_w1_2017.csv')
week2 = pd.read_csv('./1_tweets_raw/2017/jun_w2_2017.csv')
week3 = pd.read_csv('./1_tweets_raw/2017/jun_w3_2017.csv')
week4 = pd.read_csv('./1_tweets_raw/2017/jun_w4_2017.csv')

month = week1.append(week2)
month = month.append(week3)
month = month.append(week4)

month = month.drop_duplicates()

month = month.sort_values(by = 'tweet_created_at')

month = month.reset_index(drop = True)

month.to_csv('./1_tweets_raw/2017/06_2017.csv')
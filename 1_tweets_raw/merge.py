# The following python code merges the tweet data. I decided to pull the data in smaller
# batches to aviod going over the rate limit and losing the entire dataframe.
import pandas as pd
import numpy as np

week1 = pd.read_csv('./1_tweets_raw/2016/jun_w1_2016.csv')
week2 = pd.read_csv('./1_tweets_raw/2016/jun_w2_2016.csv')
week3 = pd.read_csv('./1_tweets_raw/2016/jun_w3_2016.csv')
week4 = pd.read_csv('./1_tweets_raw/2016/jun_22_2016.csv')
week5 = pd.read_csv('./1_tweets_raw/2016/jun_23_2016.csv')
week6 = pd.read_csv('./1_tweets_raw/2016/jun_24_2016.csv')
week7 = pd.read_csv('./1_tweets_raw/2016/jun_25_2016.csv')
week8 = pd.read_csv('./1_tweets_raw/2016/jun_26_2016.csv')
week9 = pd.read_csv('./1_tweets_raw/2016/jun_27_2016.csv')
week10 = pd.read_csv('./1_tweets_raw/2016/jun_28_2016.csv')
week11 = pd.read_csv('./1_tweets_raw/2016/jun_29_2016.csv')
week12 = pd.read_csv('./1_tweets_raw/2016/jun_30_2016.csv')

month = week1.append(week2)
month = month.append(week3)
month = month.append(week4)
month = month.append(week5)
month = month.append(week6)
month = month.append(week7)
month = month.append(week8)
month = month.append(week9)
month = month.append(week10)
month = month.append(week11)
month = month.append(week12)

month = month.drop_duplicates()

month = month.sort_values(by = 'tweet_created_at')

month = month.reset_index(drop = True)

month.to_csv('./1_tweets_raw/2016/06_2016.csv')
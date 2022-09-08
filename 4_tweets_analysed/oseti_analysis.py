import oseti
import pandas as pd
import numpy as np

dates = ['feb_w2', 'feb_w4', 'mar_w2', 'mar_w4', 'apr_w2', 'apr_w4', 'may_w2', 'may_w4', 'jun_w2', 'jun_w4']

for date in dates:
    analyzer = oseti.Analyzer()

    tweets = pd.read_csv('https://media.githubusercontent.com/media/jack-madison/Twitter-Sentiment-Analysis/main/all_tweets/3_tweets_cleaned/2014/' + str(date) + '_2014.csv')

    tweets['positive'] = np.nan
    tweets['negative'] = np.nan

    for x in range(len(tweets)):
        polarities = analyzer.count_polarity(str(tweets['tweet_text'][x]).replace('\n', ' ').replace('\r', ' '))

        positive = 0
        negative = 0

        for sentence in polarities:
            positive = positive + sentence['positive']
            negative = negative + sentence['negative']

        tweets['positive'][x] = positive
        tweets['negative'][x] = negative

        print(x)

    tweets['oseti_score1'] = tweets['positive'] - tweets['negative']

    tweets['oseti_score2'] = tweets['oseti_score1'] / (tweets['positive'] + tweets['negative'])

    tweets['oseti_score2'] = tweets['oseti_score2'].fillna(0)

    tweets.to_csv('./' + str(date) + '_2014_oseti.csv', index = False)